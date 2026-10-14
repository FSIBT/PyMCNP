import re

from . import _field
from . import _card
from .. import types


class Ctme(_field.Fields, _card.Card):
    """
    Represents INP ctme cards.
    """

    _KEYWORD = 'ctme'

    tme = _field.Field(types.Integer, 'Maximum amount of minutes for Monte Carlo calculation', required=True, numeric=int, invalid=lambda self, value: not value >= 0)

    _REGEX = re.compile(rf'\Actme( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
