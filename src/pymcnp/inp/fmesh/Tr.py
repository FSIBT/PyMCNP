import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Tr(_field.Fields, _option.FmeshOption):
    """
    Represents INP `tr` elements.
    """

    _KEYWORD = 'tr'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    number = _field.Field(types.Integer, 'Transformation applied to the mesh', required=True, numeric=int, invalid=lambda self, value: not (value >= 1 and value <= 999))

    _REGEX = re.compile(rf'\Atr( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
