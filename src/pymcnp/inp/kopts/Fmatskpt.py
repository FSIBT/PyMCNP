import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Fmatskpt(_field.Fields, _option.KoptsOption):
    """
    Represents INP `fmatskpt` elements.
    """

    _KEYWORD = 'fmatskpt'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    fmat_skip = _field.Field(types.Real, 'Fmat_skip', required=True)

    _REGEX = re.compile(rf'\Afmatskpt( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
