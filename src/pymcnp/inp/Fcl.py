import re

from . import _field
from . import _card
from .. import types


class Fcl(_field.Fields, _card.Card):
    """
    Represents INP `fcl` cards.
    """

    _KEYWORD = 'fcl'

    designator = _field.Field(types.Designator, 'Data card particle designator', required=True, numeric=())
    control = _field.Field.tuple(types.Real, 'Forced-collision control for cell', required=True)

    _REGEX = re.compile(rf'\Afcl:(\S+)((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
