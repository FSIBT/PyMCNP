import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Rad_0(_field.Fields, _option.SdefOption):
    """
    Represents INP `rad` elements variation #0.
    """

    _KEYWORD = 'rad'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    radial_distance = _field.Field(types.Real, 'Radial distance fo the position from POS or AXS', required=True)

    _REGEX = re.compile(rf'\Arad( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
