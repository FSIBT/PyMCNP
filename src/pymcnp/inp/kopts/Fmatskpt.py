import re

from .. import _field
from . import _option
from ... import types


class Fmatskpt(_field.Fields, _option.KoptsOption):
    """
    Represents INP `fmatskpt` elements.
    """

    _KEYWORD = 'fmatskpt'

    fmat_skip = _field.Field(types.Real, 'Fmat_skip', required=True)

    _REGEX = re.compile(rf'\Afmatskpt( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
