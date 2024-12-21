from pulp import LpProblem, LpMaximize, lpSum
from optimizer.constraints import ConstraintManager
import numpy as np
from lineups.lineups import Lineups
import pulp as plp
from collections import defaultdict



class Optimizer:
    def __init__(self, site, players, num_lineups, num_uniques, config):
        self.site = site
        self.players = players
        self.num_lineups = num_lineups
        self.num_uniques = num_uniques
        self.config = config
        self.problem = LpProblem("NFL_DFS_Optimization", LpMaximize)
        self.lp_variables = {}
        self.player_exposure = {player: 0 for player in players}  # Initialize exposure tracker

        self.position_map = {i: ["G", "F", "C", "UTIL"] for i in range(len(players))}

        # Create LP variables for each player and position
        for player in players:
            for position in player.position:
                var_name = f"{player.name}_{position}_{player.id}"
                self.lp_variables[(player, position)] = plp.LpVariable(
                    name=var_name, cat=plp.LpBinary
                )

    def adjust_roster_for_late_swap(self, lineup):
        """
        Adjusts a roster to optimize for late swap.
        Ensures players with later game times are positioned in flex spots when possible.

        :param lineup: List of tuples (player, position) representing the lineup.
        :return: Adjusted lineup.
        """
        if self.site == "fd":
            return lineup  # No late swap needed for FanDuel

        sorted_lineup = list(lineup)

        # Swap players in primary and flex positions based on game time
        def swap_if_needed(primary_pos, flex_pos):
            primary_player, primary_position = sorted_lineup[primary_pos]
            flex_player, flex_position = sorted_lineup[flex_pos]

            # Check if the primary player's game time is later than the flex player's
            if (
                primary_player.gametime > flex_player.gametime
            ):
                primary_positions = self.position_map[primary_pos]
                flex_positions = self.position_map[flex_pos]

                # Ensure both players are eligible for position swaps
                if any(
                    pos in primary_positions
                    for pos in flex_player.position
                ) and any(
                    pos in flex_positions
                    for pos in primary_player.position
                ):
                    # Perform the swap
                    sorted_lineup[primary_pos], sorted_lineup[flex_pos] = (
                        sorted_lineup[flex_pos],
                        sorted_lineup[primary_pos],
                    )

        # Iterate over positions to check and apply swaps
        for primary_pos in range(len(sorted_lineup)):
            for flex_pos in range(primary_pos + 1, len(sorted_lineup)):
                swap_if_needed(primary_pos, flex_pos)

        return sorted_lineup


    def run(self):
        """
        Run the optimization process with scaled metrics and penalized exposure.
        :return: Lineups instance containing optimized lineups.
        """
        lineups = Lineups()  # Object to store all generated lineups
        exclusion_constraints = []  # List to store uniqueness constraints

        players_by_game = defaultdict(lambda: {"team_a": [], "team_b": []})
        for player in self.players:
            if player.opponent:
                game_key = tuple(sorted([player.team, player.opponent]))
                if player.team == game_key[0]:
                    players_by_game[game_key]["team_a"].append(player)
                else:
                    players_by_game[game_key]["team_b"].append(player)

        # Weights for each component in the objective function
        baseline_fpts = None
        baseline_ownership = None
        ownership_buffer = self.config.get("ownership_buffer", 0.05)
        exposure_penalty_weights = self.config.get("exposure_penalty_weights", {})
        correlation_adjustment = self.config.get("correlation_adjustment", 0.0)
        fpts_buffer = self.config.get("fpts_buffer", 0.95)

        self.problem = LpProblem(f"NFL_DFS_Optimization", LpMaximize)

        # Reinitialize constraints for the new problem
        constraint_manager = ConstraintManager(
            self.site, self.problem, self.players, self.lp_variables, self.config
        )

        constraint_manager.add_static_constraints()  # Add static constraints

        self.problem.setObjective(
            lpSum(
                player.fpts * self.lp_variables[(player, position)]
                for player in self.players
                for position in player.position
            )
        )

        self.problem.writeLP("problem_stage1.lp")

        try:
            self.problem.solve(plp.GLPK(msg=0))
        except plp.PulpSolverError:
            print("Infeasibility during Stage 1 optimization.")
            return lineups
        
        if plp.LpStatus[self.problem.status] != "Optimal":
            print("No optimal solution found during Stage 1 optimization")
            return lineups
        
        final_vars = [
            key for key, var in self.lp_variables.items() if var.varValue == 1
        ]
        final_lineup = [(player, position) for player, position in final_vars]

        baseline_fpts = sum(player.fpts for player, _ in final_lineup)
        baseline_ownership = sum(player.ownership for player, _ in final_lineup)
        max_ownership = (1-ownership_buffer) * baseline_ownership
        min_fpts = fpts_buffer * baseline_fpts

        print(f"Baseline FPTS: {baseline_fpts}, min_fpts: {min_fpts}, baseline ownership: {baseline_ownership}, ownership limit: {max_ownership}")


        position_corr = np.array([
            [0.000, 0.056, 0.455, 0.411, -0.044, 0.271, 0.044, 0.147, 0.226, -0.424],  # QB
            [0.056, 0.000, 0.007, 0.036, 0.050, 0.044, -0.099, 0.070, 0.142, -0.201],  # RB
            [0.455, 0.007, 0.000, 0.030, -0.034, 0.147, 0.087, 0.127, -0.147, -0.234],  # WR
            [0.411, 0.036, 0.030, 0.000, -0.124, 0.226, 0.069, 0.128, 0.129, -0.126],  # TE
            [-0.044, 0.050, -0.034, -0.124, 0.000, -0.424, -0.201, -0.235, -0.126, -0.340],  # DST
            [0.271, 0.044, 0.147, 0.226, -0.424, 0.000, 0.056, 0.456, 0.411, -0.044],  # OPPQB
            [0.044, -0.099, 0.087, 0.069, -0.201, 0.056, 0.000, 0.008, 0.036, 0.050],  # OPPRB
            [0.147, 0.070, 0.127, 0.128, -0.235, 0.456, 0.008, 0.000, 0.030, -0.033],  # OPPWR
            [0.226, 0.142, -0.147, 0.129, -0.126, 0.411, 0.036, 0.030, 0.000, -0.124],  # OPPTE
            [-0.424, -0.201, -0.234, -0.126, -0.340, -0.044, 0.050, -0.033, -0.124, 0.000],  # OPPDST
        ])

        for i in range(self.num_lineups):
            if i % 10 == 0:
                print(i)
            # Step 1: Reset the optimization problem
            self.problem = LpProblem(f"NFL_DFS_Optimization_{i}", LpMaximize)

            # Reinitialize constraints for the new problem
            constraint_manager = ConstraintManager(
                self.site, self.problem, self.players, self.lp_variables, self.config
            )
            self.problem.constraints.clear()  # Clears the existing constraints

            constraint_manager.add_static_constraints()  # Add static constraints
            constraint_manager.add_optional_constraints(max_ownership, min_fpts)

            # Reapply all exclusion constraints from previous iterations
            for constraint in exclusion_constraints:
                self.problem += constraint

            # Step 2: Generate random samples for `fpts`, `boom`, and `ownership`
            random_projections = {}
            for game, teams in players_by_game.items():
                team_a_players = teams["team_a"]
                team_b_players = teams["team_b"]
                all_game_players = team_a_players + team_b_players

                num_game_players = len(all_game_players)
                game_corr = np.zeros((num_game_players, num_game_players))

                # Map positions to indices in the correlation matrix
                position_to_index = {
                    "QB": 0, "RB": 1, "WR": 2, "TE": 3, "DST": 4,
                    "OPPQB": 5, "OPPRB": 6, "OPPWR": 7, "OPPTE": 8, "OPPDST": 9,
                }

                # Build the correlation matrix for the current game
                for i, player_i in enumerate(all_game_players):
                    for j, player_j in enumerate(all_game_players):
                        pos_i = player_i.position[0]  # Assume single position
                        pos_j = player_j.position[0]
                        team_i = player_i.team
                        team_j = player_j.team

                        if team_i == team_j:
                            # Same team correlation
                            game_corr[i, j] = position_corr[
                                position_to_index[pos_i], position_to_index[pos_j]
                            ]
                        else:
                            # Cross-team correlation
                            game_corr[i, j] = position_corr[
                                position_to_index[f"OPP{pos_i}"], position_to_index[f"OPP{pos_j}"]
                            ]

                # Ensure positive semi-definiteness
                epsilon = 1e-10
                game_corr = (game_corr + game_corr.T) / 2
                np.fill_diagonal(game_corr, 1.0)
                eigvals = np.linalg.eigvalsh(game_corr)
                if np.min(eigvals) < 0:
                    game_corr += (-np.min(eigvals) + epsilon) * np.eye(num_game_players)

                # Generate correlated random values
                mean_fpts = [player.fpts for player in all_game_players]
                stddevs = [player.stddev * self.config["randomness_amount"] / 100 for player in all_game_players]
                uncorrelated = np.random.normal(loc=mean_fpts, scale=stddevs, size=num_game_players)
                L = np.linalg.cholesky(game_corr)
                correlated = np.dot(L, uncorrelated)

                # Apply the correlation adjustment
                adjusted_projections = (1 - correlation_adjustment) * uncorrelated + correlation_adjustment * correlated

                # Assign projections back to players
                for i, player in enumerate(all_game_players):
                    for position in player.position:
                        random_projections[(player, position)] = adjusted_projections[i]

            # Step 3: Calculate global max for scaling based on random samples
            max_fpts = max(random_projections.values(), default=1)  # Avoid division by zero

            # Step 4: Scale each variable to range [0, 1]
            scaled_projections = {
                key: value / max_fpts for key, value in random_projections.items()
            }

            # Step 5: Set the scaled and penalized objective function
            self.problem.setObjective(
                lpSum(
                    scaled_projections[(player, position)] 
                    * self.lp_variables[(player, position)]
                    for player in self.players
                    for position in player.position
                )
            )
            self.problem.writeLP("problem.lp")

            # Solve the problem
            try:
                self.problem.solve(plp.GLPK(msg=0))
            except plp.PulpSolverError:
                print(f"Infeasibility reached during optimization. Only {len(lineups.lineups)} lineups generated.")
                break

            if plp.LpStatus[self.problem.status] != "Optimal":
                print(f"Infeasibility reached during optimization. Only {len(lineups.lineups)} lineups generated.")
                break

            # Step 6: Extract and save the final lineup
            final_vars = [
                key for key, var in self.lp_variables.items() if var.varValue == 1
            ]
            final_lineup = [(player, position) for player, position in final_vars]
            final_lineup = self.adjust_roster_for_late_swap(final_lineup)
            lineups.add_lineup(final_lineup)

            # Step 7: Update player exposure
            for player, position in final_vars:
                self.player_exposure[player] += 1

            # Step 8: Add exclusion constraint for uniqueness
            player_ids = [player.id for player, _ in final_vars]
            player_keys_to_exclude = [
                (p, pos) for p in self.players if p.id in player_ids for pos in p.position
            ]
            exclusion_constraint = lpSum(
                self.lp_variables[(player, pos)] for player, pos in player_keys_to_exclude
            ) <= len(final_vars) - self.num_uniques
            exclusion_constraints.append(exclusion_constraint)

        return lineups
    

    






