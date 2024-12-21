from pulp import lpSum, LpVariable


class ConstraintManager:
    def __init__(self, site, problem, players, lp_variables, config):
        self.site = site
        self.problem = problem
        self.players = players
        self.lp_variables = lp_variables
        self.config = config

    def add_salary_constraints(self):
        max_salary = 50000 if self.site == "dk" else 60000
        min_salary = 49500 if self.site == "dk" else 59000

        self.problem += lpSum(
            player.salary * self.lp_variables[(player, position)]
            for player in self.players
            for position in player.position
        ) <= max_salary, "Max_Salary"

        self.problem += lpSum(
            player.salary * self.lp_variables[(player, position)]
            for player in self.players
            for position in player.position
        ) >= min_salary, "Min_Salary"

    def add_position_constraints(self):
        # Hard-coded position constraints
        if self.site == "dk":
            position_limits = {
                "QB": 1, "RB": 2, "WR": 3, "TE": 1, "FLEX": 1, "DST": 1
            }
        else:  # Assuming "fd"
            return

        for pos, limit in position_limits.items():
            eligible = [(player, pos) for player in self.players if pos in player.position]
            self.problem += lpSum(self.lp_variables[key] for key in eligible) == limit, f"Position_{pos}"

    def add_global_team_limit(self):
        global_limit = self.config.get("global_team_limit")
        if global_limit:
            for team in set(player.team for player in self.players):
                eligible = [
                    (player, pos) for player in self.players for pos in player.position if player.team == team
                ]
                self.problem += lpSum(self.lp_variables[key] for key in eligible) <= global_limit, f"Global_Team_{team}"

    def exclude_exact_lineup(self, lineup, lineup_index):
        """
        Add a constraint to exclude the exact lineup from being selected again.
        :param lineup: List of (player, position) tuples in the lineup.
        :param lineup_index: The index of the lineup being excluded.
        """
        constraint_name = f"Exclude_Lineup_{lineup_index}"
        self.problem += (
            lpSum(self.lp_variables[(player, position)] for player, position in lineup) <= len(lineup) - 1,
            constraint_name
        )
    def add_qb_selection_variables(self):
        """
        Centralize the logic to create and store binary variables for whether a QB is selected.
        """
        self.qb_selected_vars = {}  # Dictionary to store QB selection variables

        for qb, _ in [
            (player, pos) for player in self.players for pos in player.position if pos == "QB"
        ]:
            if qb.name not in self.qb_selected_vars:
                # Create the binary variable for whether the QB is selected
                qb_selected = LpVariable(f"qb_{qb.name}_selected", 0, 1, cat="Binary")

                # Link the QB selection variable to the QB LP variable
                self.problem += (
                    qb_selected == lpSum(self.lp_variables[(qb, "QB")]),
                    f"Select_QB_{qb.name}"
                )

                # Store the variable for reuse
                self.qb_selected_vars[qb.name] = qb_selected

    def add_qb_stack_constraints(self):
        """
        Add constraints to enforce stacking of players from the same team as the QB,
        only if the QB is chosen in the lineup.
        """
        qb_stack_config = self.config.get("qb_stack_requirements", {})
        min_stack = qb_stack_config.get("min_stack", 1)  # Default to 1
        eligible_positions = qb_stack_config.get("positions", ["WR", "TE"])  # Default to WR and TE

        for qb, _ in [
            (player, pos) for player in self.players for pos in player.position if pos == "QB"
        ]:
            # Get eligible stack players (WR/TE) from the same team as the QB
            eligible_stack_players = [
                (player, pos)
                for player in self.players
                for pos in player.position
                if pos in eligible_positions and player.team == qb.team
            ]

            if eligible_stack_players:
                # Reuse the pre-defined QB selection variable
                qb_selected = self.qb_selected_vars[qb.name]

                # Enforce stacking only if the QB is selected
                self.problem += (
                    lpSum(self.lp_variables[key] for key in eligible_stack_players)
                    >= min_stack * qb_selected,
                    f"QB_Stack_{qb.name}_Min_stack_{min_stack}",
                )



    def add_qb_runback_constraints(self):
        """
        Add constraints to enforce a 'runback' of at least one player from the opposing team of the QB,
        only if the QB is selected in the lineup.
        """
        qb_runback_config = self.config.get("qb_runback_requirements", {})
        min_runback = qb_runback_config.get("min_runback", 1)  # Default to 1
        eligible_positions = qb_runback_config.get("positions", ["WR", "RB"])  # Default to WR and RB

        for qb, _ in [
            (player, pos) for player in self.players for pos in player.position if pos == "QB"
        ]:
            # Identify the opposing team for the QB
            opposing_team = qb.opponent

            # Get eligible runback players (e.g., WR/RB) from the opposing team
            eligible_runback_players = [
                (player, pos)
                for player in self.players
                for pos in player.position
                if pos in eligible_positions and player.team == opposing_team
            ]

            if eligible_runback_players:
                # Reuse the pre-defined QB selection variable
                qb_selected = self.qb_selected_vars[qb.name]

                # Enforce runback only if the QB is selected
                self.problem += (
                    lpSum(self.lp_variables[key] for key in eligible_runback_players)
                    >= min_runback * qb_selected,
                    f"QB_Runback_{qb.name}_Min_runback_{min_runback}",
                )




    def add_offense_vs_defense_constraints(self):
        """
        Add a constraint to limit the number of offensive players from the opposing team
        if the corresponding defense (`DST`) is selected.
        """
        max_offense_vs_defense = self.config.get("max_offense_vs_defense", 3)  # Default to 3
        if max_offense_vs_defense is None:
            return  # If not specified, no constraint is applied

        # Loop through each defense (DST) player
        for defense in [p for p in self.players if "DST" in p.position]:
            # Identify the opposing team for this defense
            opposing_team = defense.opponent

            # Get all offensive players from the opposing team
            offensive_players = [
                (player, pos)
                for player in self.players
                for pos in player.position
                if player.team == opposing_team and pos != "DST"
            ]

            if offensive_players:
                # Create a binary decision variable for whether the defense (DST) is selected
                defense_selected = LpVariable(f"defense_{defense.team}_selected", 0, 1, cat="Binary")

                # Link the defense selection variable with the defense LP variable
                self.problem += (
                    defense_selected == lpSum(self.lp_variables[(defense, pos)] for pos in defense.position),
                    f"Select_Defense_{defense.team}"
                )

                # Limit offensive players if the defense is selected
                constraint_name = f"Offense_vs_Defense_{defense.team}_vs_{opposing_team}"
                self.problem += (
                    lpSum(self.lp_variables[(player, pos)] for player, pos in offensive_players)
                    <= max_offense_vs_defense + (1 - defense_selected) * len(offensive_players),
                    constraint_name
                )
            else:
                print(f"No offensive players found for defense {defense.team} against {opposing_team}")




    def add_single_player_constraints(self):
        for player in self.players:
            self.problem += lpSum(
                self.lp_variables[(player, position)] for position in player.position
            ) <= 1, f"Single_Use_{player.name}"

    def add_conditional_team_limit_with_qb(self):
        """
        Add a constraint to limit the number of players from a team unless paired with the QB.
        This applies conditional constraints based on which QB is selected.
        """
        max_non_qb_team_limit = self.config.get("max_non_qb_team_limit", 2)  # Default to 2
        qb_team_vars = {}  # This will store QB team selections

        # Iterate over all QBs to create conditional constraints
        for player in self.players:
            if "QB" in player.position:  # If the player is a QB
                qb_team = player.team

                # Check if the QB is selected
                qb_team_vars[qb_team] = LpVariable(f"team_{qb_team}_selected", 0, 1, cat='Binary')

                # Now apply constraints for players from that team
                team_players = [
                    (p, pos) for p in self.players for pos in p.position if p.team == qb_team and p != player
                ]

                # Apply conditional team limit for non-QB players of that team
                for team_player, pos in team_players:
                    # Make the constraint name unique by including the team, QB, and position
                    constraint_name = f"Team_Limit_With_QB_{qb_team}_{team_player.name}_{pos}"
                    self.problem += (
                        self.lp_variables[(team_player, pos)] <= (
                            max_non_qb_team_limit + max_non_qb_team_limit * qb_team_vars[qb_team]
                        ),
                        constraint_name  # Use a dynamic constraint name based on position
                    )

    def add_static_constraints(self):
        """
        Add all static constraints for the optimizer.
        """
        self.add_salary_constraints()
        self.add_position_constraints()
        self.add_global_team_limit()
        self.add_single_player_constraints()

        # Add QB-related constraints
        self.add_qb_selection_variables()  # Create QB selection variables first
        self.add_qb_stack_constraints()
        self.add_qb_runback_constraints()

        self.add_conditional_team_limit_with_qb()
        self.add_offense_vs_defense_constraints()


    def add_optional_constraints(self, max_ownership=None, min_fpts=None):
        '''
        Add optional constraints such as ownership maximum and FPTS minimum. 
        :param max_ownership: Maximum allowable cumulative ownership.
        :param min_fpts: min required cumulative fpts. 
        '''
        if max_ownership is not None:
            lineup_ownership = lpSum(
                player.ownership * self.lp_variables[(player, position)]
                for player in self.players
                for position in player.position
            )
            self.problem += lineup_ownership <= max_ownership, "Max_Ownership"

        if min_fpts is not None: 
            lineups_fpts = lpSum(
                player.fpts * self.lp_variables[(player, position)]
                for player in self.players
                for position in player.position
            )
            self.problem += lineups_fpts >= min_fpts, "Min_FPTS"



