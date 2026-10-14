import re

from .. import _field
from . import _option
from ... import types


class Fmatny(_field.Fields, _option.KoptsOption):
    """
    Represents INP `fmatny` elements.
    """

    _KEYWORD = 'fmatny'

    fmat_ny = _field.Field(types.Real, 'Fmat_ny', required=True)

    _REGEX = re.compile(rf'\Afmatny( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
