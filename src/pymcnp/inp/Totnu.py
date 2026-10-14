import re

from . import _field
from . import _card
from .. import types


class Totnu(_field.Fields, _card.Card):
    """
    Represents INP `totnu` cards.
    """

    _KEYWORD = 'totnu'

    no = _field.Field(types.String, 'Delay fission sampling on/off', numeric=(), invalid=lambda self, value: value is not None and (not value == 'no'))

    _REGEX = re.compile(rf'\Atotnu( {types.String._REGEX.pattern[2:-2]})?\Z', re.IGNORECASE)
