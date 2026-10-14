import re

from . import _field
from . import uran
from . import _card


class Uran(_field.Fields, _card.Card):
    """
    Represents INP `uran` cards.
    """

    _KEYWORD = 'uran'

    transformations = _field.Field.tuple(uran.Stochastic, 'Tuple of stochastic transformations', required=True, numeric=())

    _REGEX = re.compile(r'\Auran((?: \S+ \S+ \S+ \S+)+?)\Z', re.IGNORECASE)
