import pandas


class Frame:
    def __init__(self):
        self.frame_dict = None
        self.df = None

    def define(self, headers: list[str]):
        self.frame_dict = {header: [] for header in headers}

    def create_df(self):
        if self.frame_dict:
            self.df = pandas.DataFrame(self.frame_dict)
        else:
            raise Exception(
                "Attempted to create a pandas.DataFrame but Frame.frame_dict does not exist. Call Frame.define()."
            )

    def append(self, row: dict[str, float]):
        if self.frame_dict:
            for header in self.frame_dict:
                if header in row:
                    self.frame_dict[header].append(row[header])
                else:
                    self.frame_dict[header].append(None)
        else:
            raise Exception(
                "Attempted to append to frame_dict but it does not exist. Call Frame.define()."
            )
