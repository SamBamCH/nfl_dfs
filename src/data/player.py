class Player:
    def __init__(self, name, team, opp, position, salary, stddev, floor, ceiling, boom, bust, optimal, own, fpts):
        self.name = name
        self.team = team
        self.opponent = opp
        self.position = position
        self.salary = salary
        self.stddev = stddev
        self.floor = floor
        self.ceiling = ceiling
        self.boom = boom
        self.bust = bust
        self.optimal = optimal
        self.ownership = own
        self.std_ownership = own / 10
        self.fpts = fpts
        self.id = None
        self.gametime = None

    def __str__(self):
        return f"Player(name={self.name},team={self.team},opp={self.opponent}, position={self.position} fpts={self.fpts}, own={self.ownership}, id={self.id})"






