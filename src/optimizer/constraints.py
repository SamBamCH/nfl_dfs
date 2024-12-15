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
        min_salary = 49000 if self.site == "dk" else 59000

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

    def add_single_player_constraints(self):
        for player in self.players:
            self.problem += lpSum(
                self.lp_variables[(player, position)] for position in player.position
            ) <= 1, f"Single_Use_{player.name}"

    def add_static_constraints(self):
        '''
        This is used for static constraints for the site you are optimizing for (i.e. draftkings, nba). 
        '''
        self.add_salary_constraints()
        self.add_position_constraints()
        self.add_global_team_limit()
        self.add_single_player_constraints()


