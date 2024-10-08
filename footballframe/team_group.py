from .team import Team


class Group:
    def __init__(self):
        self.name = None
        self.abr = None
        self.members = []

    def set_into(self, name: str, abr: str):
        self.name = name
        self.abr = abr

    def add_member(self, member):
        self.members.append(member)

