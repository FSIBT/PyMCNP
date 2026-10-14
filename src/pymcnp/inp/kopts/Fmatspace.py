import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Fmatspace(_field.Fields, _option.KoptsOption):
    """
    Represents INP `fmatspace` elements.
    """

    _KEYWORD = 'fmatspace'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    fmat_space = _field.Field(types.Real, 'Fmat_space', required=True)

    _REGEX = re.compile(rf'\Afmatspace( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
