from pulp import lpSum


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
    def add_qb_stack_constraints(self):
        """
        Add constraints to enforce stacking of players from the same team as the QB.
        """
        qb_stack_config = self.config.get("qb_stack_requirements", {})
        min_stack = qb_stack_config.get("min_stack", 1)  # Default to 1
        eligible_positions = qb_stack_config.get("positions", ["WR", "TE"])  # Default to WR and TE

        # Get all QBs
        qb_vars = [
            (player, pos) for player in self.players for pos in player.position if pos == "QB"
        ]

        for qb, _ in qb_vars:
            # Get eligible stack players (WR/TE) from the same team as the QB
            eligible_stack_players = [
                (player, pos)
                for player in self.players
                for pos in player.position
                if pos in eligible_positions and player.team == qb.team
            ]

            # Enforce minimum stack size with the QB
            if eligible_stack_players:
                self.problem += (
                    lpSum(self.lp_variables[key] for key in eligible_stack_players)
                    >= min_stack * self.lp_variables[(qb, "QB")],
                    f"QB_Stack_{qb.name}_Min_{min_stack}",
                )

    def add_qb_runback_constraints(self):
        """
        Add constraints to enforce a 'runback' of at least one player from the opposing team of the QB.
        """
        qb_runback_config = self.config.get("qb_runback_requirements", {})
        min_runback = qb_runback_config.get("min_runback", 1)  # Default to 1
        eligible_positions = qb_runback_config.get("positions", ["WR", "RB"])  # Default to WR and RB

        # Get all QBs
        qb_vars = [
            (player, pos) for player in self.players for pos in player.position if pos == "QB"
        ]

        for qb, _ in qb_vars:
            # Identify the opposing team for the QB
            opposing_team = qb.opponent  # Assuming players have an `opponent` attribute

            # Get eligible runback players (e.g., WR/RB) from the opposing team
            eligible_runback_players = [
                (player, pos)
                for player in self.players
                for pos in player.position
                if pos in eligible_positions and player.team == opposing_team
            ]

            # Enforce minimum runback size for the opposing team
            if eligible_runback_players:
                self.problem += (
                    lpSum(self.lp_variables[key] for key in eligible_runback_players)
                    >= min_runback * self.lp_variables[(qb, "QB")],
                    f"QB_Runback_{qb.name}_Min_{min_runback}",
                )

    def add_offense_vs_defense_constraints(self):
        """
        Add a constraint to limit the number of offensive players against a selected defense.
        """
        max_offense_vs_defense = self.config.get("max_offense_vs_defense", None)
        if max_offense_vs_defense is None:
            return  # If not specified, no constraint is applied

        for defense in [p for p in self.players if "DST" in p.position]:
            # Get all offensive players playing against this defense's team
            offensive_players = [
                (player, pos)
                for player in self.players
                for pos in player.position
                if player.team == defense.opponent and pos != "DST"
            ]

            if offensive_players:
                # If the defense is selected, limit the number of offensive players from its opposing team
                self.problem += (
                    lpSum(self.lp_variables[key] for key in offensive_players)
                    <= max_offense_vs_defense * self.lp_variables[(defense, "DST")],
                    f"Offense_vs_Defense_{defense.team}",
                )



    def add_single_player_constraints(self):
        for player in self.players:
            self.problem += lpSum(
                self.lp_variables[(player, position)] for position in player.position
            ) <= 1, f"Single_Use_{player.name}"

    def add_team_limit_with_qb(self):
        """
        Add a constraint to limit the number of players from a team unless paired with the QB.
        """
        max_non_qb_team_limit = self.config.get("max_non_qb_team_limit", 2)  # Default to 2

        # Iterate over all teams
        for team in set(player.team for player in self.players):
            # Get all players from the team
            team_players = [
                (player, pos)
                for player in self.players
                for pos in player.position
                if player.team == team
            ]

            # Identify the QB(s) for the team
            qb_vars = [
                (player, pos)
                for player, pos in team_players
                if pos == "QB"
            ]

            # Exclude the QB from the rest of the players
            non_qb_players = [
                (player, pos)
                for player, pos in team_players
                if pos != "QB"
            ]

            if qb_vars and non_qb_players:
                # Ensure the number of non-QB players is limited unless the QB is selected
                self.problem += (
                    lpSum(self.lp_variables[key] for key in non_qb_players)
                    <= max_non_qb_team_limit
                    + max_non_qb_team_limit * lpSum(self.lp_variables[key] for key in qb_vars),
                    f"Team_Limit_With_QB_{team}",
                )

    def add_static_constraints(self):
        '''
        This is used for static constraints for the site you are optimizing for (i.e. draftkings, nba). 
        '''
        self.add_salary_constraints()
        self.add_position_constraints()
        self.add_global_team_limit()
        self.add_single_player_constraints()
        self.add_qb_stack_constraints()
        self.add_qb_runback_constraints()
        # self.add_offense_vs_defense_constraints()



