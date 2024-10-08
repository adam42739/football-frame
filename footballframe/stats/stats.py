import pandas
from . import categories
from . import types


class Frame:
    """
    ===========
    Stats.Frame
    ===========

    A class for general football stat keeping.

    Usage
    -----

    First create and define a frame by category. Mixing stats from multiple categories into a single frame is not recommended.

    >>> frame = Frame()
    >>> frame.define(categories.PASSING)

    Append rows of stats (typically after each play) to the frame

    >>> frame.append({passing.CMP: 1, passing.ATT: 1, passing.YDS: 10})

    Create a `pandas.DataFrame` from the `Frame` object. Creating a `pandas.DataFrame` is time consuming and should not be done frequently.

    >>> frame.create_df

    Aggregate all rows of the frame into totals/summary stats.

    >>> frame.agg_df()

    Access the aggregated summary stats.

    >>> frame.aggregated

    """

    def __init__(self):
        self.category = None
        self.frame_dict = None
        self.df = pandas.DataFrame

    def define(self, category: str, headers: list[str] = None):
        """
        Define the stats included in the `Frame`.

        Parameters
        ----------

        category : str
            The stats category to create the `Frame` for.

        headers : list[str] = None
            Provide if wishing to only include specific stats from the provided category. Including stats from other categories is not recommended.
        """
        if not headers:
            headers = categories.STAT_DICTS[category]
        self.frame_dict = {header: [] for header in headers}
        self.category = category

    def create_df(self):
        """
        Create a `pandas.DataFrame` from associated with the `Frame`. Accessible as `Frame.df`.
        """
        if self.frame_dict:
            self.df = pandas.DataFrame(self.frame_dict)
        else:
            raise Exception(
                "Attempted to create a pandas.DataFrame but Frame.frame_dict does not exist. Call Frame.define()."
            )

    def append(self, row: dict[str, float]):
        """
        Append a row of stats to the `Frame`.

        Parameters
        ----------

        row : dict[str, float]
            A dictionary containing stats to append to the `Frame`.
            If a stat is present in the `Frame` but not in `row`, `None` is used in place of the missing value.
            Typically called after each play.

        Example Usage
        -------------

        After a play consisting of a 10 yard completion. Update to the passer's stats:

        >>> frame.append({passing.CMP: 1, passing.ATT: 1, passing.YDS: 10})

        """
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
        """
        Aggregate the `Frame` to create a `dict` of totals/summary stats. Aggregated `dict` accessible as `frame.aggregated`.
        """
        if not self.df.empty:
            self.aggregated = {}
            self._agg_accum()
            self._agg_other()
        else:
            raise Exception(
                "Attempted to aggregate Frame.df but it does not exist. Call Frame.create_df()."
            )
