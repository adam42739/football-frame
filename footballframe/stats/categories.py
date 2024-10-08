from . import defense
from . import kicking
from . import passing
from . import punting
from . import receiving
from . import returning
from . import rushing
from . import scoring


PASSING = "Passing"
RUSHING = "Rushing"
RECEIVING = "Receiving"
DEFENSE = "Defense"
SCORING = "Scoring"
RETURNING = "Returning"
KICKING = "Kicking"
PUNTING = "Punting"

LIST = [
    PASSING,
    RUSHING,
    RECEIVING,
    DEFENSE,
    SCORING,
    RETURNING,
    KICKING,
    PUNTING,
]

STAT_DICTS = {
    PASSING: passing.DICT,
    RUSHING: rushing.DICT,
    RECEIVING: receiving.DICT,
    DEFENSE: defense.DICT,
    SCORING: scoring.DICT,
    RETURNING: returning.DICT,
    KICKING: kicking.DICT,
    PUNTING: punting.DICT,
}
