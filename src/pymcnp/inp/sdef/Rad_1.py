import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Rad_1(_field.Fields, _option.SdefOption):
    """
    Represents INP `rad` elements variation #1.
    """

    _KEYWORD = 'rad'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    radial_distance = _field.Field(types.Distribution, 'Radial distance fo the position from POS or AXS', required=True, numeric=())

    _REGEX = re.compile(rf'\Arad( {types.Distribution._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
