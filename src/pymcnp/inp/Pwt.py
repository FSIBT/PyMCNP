import re

from . import _field
from . import _card
from .. import types


class Pwt(_field.Fields, _card.Card):
    """
    Represents INP `pwt` cards.
    """

    _KEYWORD = 'pwt'

    weights = _field.Field.tuple(types.Real, 'Relative threshold weight of photons produced at neutron collisions in cell', required=True)

    _REGEX = re.compile(rf'\Apwt((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
