import pandas
from . import categories
from . import types


class Frame:
    def __init__(self):
        self.category = None
        self.frame_dict = None
        self.df = pandas.DataFrame

    def define(self, category: str, headers: list[str] = None):
        if not headers:
            headers = categories.STAT_DICTS[category]
        self.frame_dict = {header: [] for header in headers}
        self.category = category

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
                "Attempted to append to Frame.frame_dict but it does not exist. Call Frame.define()."
            )

    def _agg_accum(self):
        for header in self.df.columns:
            if categories.STAT_DICTS[self.category][header][types.TYPE] == types.ACCUM:
                agg_val = self.df[header].sum()
                self.aggregated[header] = agg_val

    def _agg_other(self):
        for header in self.df.columns:
            if categories.STAT_DICTS[self.category][header][types.TYPE] == types.AVG:
                X = 0
                for X_header in categories.STAT_DICTS[self.category][header][
                    types.PARAM
                ]["X"]:
                    X += self.aggregated[X_header]
                Y = 0
                for Y_header in categories.STAT_DICTS[self.category][header][
                    types.PARAM
                ]["Y"]:
                    Y += self.aggregated[Y_header]
                agg_val = X / Y
                self.aggregated[header] = agg_val
            elif categories.STAT_DICTS[self.category][header][types.TYPE] == types.MAX:
                agg_val = self.df[header].max()
                self.aggregated[header] = agg_val

    def agg_df(self):
        if not self.df.empty:
            self.aggregated = {}
            self._agg_accum()
            self._agg_other()
        else:
            raise Exception(
                "Attempted to aggregate Frame.df but it does not exist. Call Frame.create_df()."
            )
