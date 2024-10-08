import datetime


class Player:
    def __init__(self):
        pass

    def set_info(
        self,
        first_name: str,
        last_name: str,
        birth_date: datetime.datetime,
        height: int,
        weight: int,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.height = height
        self.weight = weight
