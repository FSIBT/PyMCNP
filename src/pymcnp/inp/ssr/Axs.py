import re

from .. import _field
from . import _option
from ... import types


class Axs(_field.Fields, _option.SsrOption):
    """
    Represents INP `axs` elements.
    """

    _KEYWORD = 'axs'

    cosines = _field.Field.tuple(types.Real, 'Direction cosines defining', required=True)

    _REGEX = re.compile(rf'\Aaxs((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
