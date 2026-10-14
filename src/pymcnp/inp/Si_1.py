import re

from . import _field
from . import _card
from .. import types


class Si_1(_field.Fields, _card.Card):
    """
    Represents INP `si` elements variation #1.
    """

    _KEYWORD = 'si'

    _ORDER = ('suffix', 'information', 'option')

    suffix = _field.Field(types.Integer, 'Data card option suffix', required=True, numeric=int)
    option = _field.Field(types.String, 'Information kind setting', numeric=())
    information = _field.Field.tuple(types.Real, 'Particle source information', required=True)

    _REGEX = re.compile(rf'\Asi(\d+)( [hlas])?((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
