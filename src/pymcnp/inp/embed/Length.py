import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Length(_field.Fields, _option.EmbedOption):
    """
    Represents INP `length` elements.
    """

    _KEYWORD = 'length'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    factor = _field.Field(types.Real, 'Conversion factor to centimeters for all mesh dimentions', required=True, invalid=lambda self, value: not value > 0)

    _REGEX = re.compile(rf'\Alength( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
