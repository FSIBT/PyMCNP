import re

from .. import _field
from . import _option
from ... import types


class Field(_field.Fields, _option.BfldOption):
    """
    Represents INP `field` elements.
    """

    _KEYWORD = 'field'

    strength_gradient = _field.Field(types.Real, 'Magnetic field strength/gradient', required=True)

    _REGEX = re.compile(rf'\Afield( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
