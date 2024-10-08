import datetime


class Coach:
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.birth_date = None

    def set_info(self, first_name: str, last_name: str, birth_date: datetime.datetime):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
