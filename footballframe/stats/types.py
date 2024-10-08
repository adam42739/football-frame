"""
=====================
Stat Types Submodule
=====================

Use for defining new stats inside another submodele.

Example
-------

Update the `passing` module to include a stat named CMPP which computes the passer's completion percentage by taking CMP over ATT.

>>> passing.CMPP = "CMPP"
>>> passing.DICT[passing.CMPP] = {types.TYPE: types.AVG, types.PARAM: {"X": [passing.CMP], "Y": [passing.ATT]}}

"""

TYPE = "type"
PARAM = "param"


ACCUM = 1
AVG = 2
MAX = 3
