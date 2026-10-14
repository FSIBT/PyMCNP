import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Loc_0(_field.Fields, _option.SdefOption):
    """
    Represents INP `loc` elements variation #0.
    """

    _KEYWORD = 'loc'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    latitude = _field.Field(types.Real, 'Latitude for cosmic source', required=True, invalid=lambda self, value: not (value >= -0 and value <= 90))
    longitude = _field.Field(types.Real, 'Longitude for cosmic source', required=True, invalid=lambda self, value: not (value >= -0 and value <= 180))
    altitude = _field.Field(types.Real, 'Altitude for cosmic source', required=True, invalid=lambda self, value: not 0 <= value)

    _REGEX = re.compile(rf'\Aloc( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
