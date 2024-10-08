from .player import Player
from .coach import Coach


class Team:
    def __init__(self):
        self.name = None
        self.abr = None
        self.players = []
        self.coaches = []

    def set_info(self, name: str, abr: str):
        self.name = name
        self.abr = abr
        self.info = True

    def add_coach(self, coach: Coach):
        self.coaches.append(coach)

    def add_player(self, player: Player):
        self.players.append(player)
