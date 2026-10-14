import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Fmatny(_field.Fields, _option.KoptsOption):
    """
    Represents INP `fmatny` elements.
    """

    _KEYWORD = 'fmatny'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    fmat_ny = _field.Field(types.Real, 'Fmat_ny', required=True)

    _REGEX = re.compile(rf'\Afmatny( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
