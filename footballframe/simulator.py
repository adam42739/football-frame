from .team import Team


LOC_TEAM1 = 0
LOC_TEAM2 = 1
LOC_NEUTRAL = 2


class Matchup:
    def __init__(self):
        pass

    def create(self, team1: Team, team2: Team, loc: int):
        self.team1 = team1
        self.team2 = team2
        self.loc = loc



class Week:
    def __init__(self):
        self.matchups: dict[int, Matchup] = {}

    def add_matchup(self, mid: int, matchup: Matchup):
        self.matchups[mid] = matchup


class Season:
    def __init__(self):
        self.weeks: dict[int, Week] = {}

    def add_week(self, week_num: int, week: Week):
        self.weeks[week_num] = week
