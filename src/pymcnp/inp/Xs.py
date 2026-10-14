import re

from . import _field
from . import _card
from .. import types


class Xs(_field.Fields, _card.Card):
    """
    Represents INP `xs` cards.
    """

    _KEYWORD = 'xs'

    suffix = _field.Field(types.Integer, 'Data card option suffix', required=True, numeric=int)
    weight_ratios = _field.Field.tuple(types.Substance, 'Tuple of atomic weight ratios', required=True, numeric=())

    _REGEX = re.compile(rf'\Axs(\d+)((?: {types.Substance._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
