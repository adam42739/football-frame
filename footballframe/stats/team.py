from . import types


W = "W"
L = "L"
T = "T"
PCT = "PCT"
PF = "PF"
PA = "PA"
NET_PTS = "Net Pts"
HOMEW = "Home W"
HOMEL = "Home L"
HOMET = "Home T"
AWAYW = "Away W"
AWAYL = "Away L"
AWAYT = "Away T"
DIVW = "Div W"
DIVL = "Div L"
DIVT = "Div T"
CONFW = "Conf W"
CONFL = "Conf L"
CONFT = "Conf T"
NON_CONFW = "Non-Conf W"
NON_CONFL = "Non-Conf L"
NON_CONFT = "Non-Conf T"


DICT = {
    W: {types.TYPE: types.ACCUM, types.PARAM: None},
    L: {types.TYPE: types.ACCUM, types.PARAM: None},
    T: {types.TYPE: types.ACCUM, types.PARAM: None},
    PCT: {types.TYPE: types.AVG, types.PARAM: {"X": [W], "Y": [W, L, T]}},
    PF: {types.TYPE: types.ACCUM, types.PARAM: None},
    PA: {types.TYPE: types.ACCUM, types.PARAM: None},
    NET_PTS: {types.TYPE: types.ACCUM, types.PARAM: None},
    HOMEW: {types.TYPE: types.ACCUM, types.PARAM: None},
    HOMEL: {types.TYPE: types.ACCUM, types.PARAM: None},
    HOMET: {types.TYPE: types.ACCUM, types.PARAM: None},
    AWAYW: {types.TYPE: types.ACCUM, types.PARAM: None},
    AWAYL: {types.TYPE: types.ACCUM, types.PARAM: None},
    AWAYT: {types.TYPE: types.ACCUM, types.PARAM: None},
    DIVW: {types.TYPE: types.ACCUM, types.PARAM: None},
    DIVL: {types.TYPE: types.ACCUM, types.PARAM: None},
    DIVT: {types.TYPE: types.ACCUM, types.PARAM: None},
    CONFW: {types.TYPE: types.ACCUM, types.PARAM: None},
    CONFL: {types.TYPE: types.ACCUM, types.PARAM: None},
    CONFT: {types.TYPE: types.ACCUM, types.PARAM: None},
    NON_CONFW: {types.TYPE: types.ACCUM, types.PARAM: None},
    NON_CONFL: {types.TYPE: types.ACCUM, types.PARAM: None},
    NON_CONFT: {types.TYPE: types.ACCUM, types.PARAM: None},
}
