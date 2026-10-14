import re

from .. import _field
from . import _option
from ... import types


class Axs(_field.Fields, _option.BfldOption):
    """
    Represents INP `axs` elements.
    """

    _KEYWORD = 'axs'

    vector = _field.Field.tuple(types.Real, 'Direction of the cosines of the quadropole beam axis', required=True)

    _REGEX = re.compile(rf'\Aaxs((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
