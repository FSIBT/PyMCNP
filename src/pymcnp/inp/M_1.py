import re

from . import _field
from . import _card
from .. import types


class M_1(_field.Fields, _card.Card):
    """
    Represents INP `m` elements variation #1.
    """

    _KEYWORD = 'm'

    suffix = _field.Field(types.Integer, 'Data card option suffix', required=True, numeric=int)
    abx = _field.Field(types.String, 'Material library', required=True, numeric=())

    _REGEX = re.compile(rf'\Am(\d+)( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
