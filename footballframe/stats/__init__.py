"""
==============
Football Stats
==============

The `stats` subpackage allows for keeping track of player and team stats while simulating. Use the `stats.Frame()` class for general stat keeping.

Available Submodules
--------------------

Categories:

>>> import stats.categories as categories

Defense:

>>> import stats.defense as defense

Kicking:

>>> import stats.kicking as kicking

Passing:

>>> import stats.passing as passing

Punting:

>>> import stats.punting as punting

Receiving:

>>> import stats.receiving as receiving

Returning:

>>> import stats.returning as returning

Rushing:

>>> import stats.rushing as rushing

Scoring:

>>> import stats.scoring as scoring

Team:

>>> import stats.team as team

"""

from . import categories
from . import defense
from . import kicking
from . import passing
from . import punting
from . import receiving
from . import returning
from . import rushing
from . import scoring
from . import team
from .stats import Frame
