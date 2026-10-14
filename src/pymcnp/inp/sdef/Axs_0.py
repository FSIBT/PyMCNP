import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Axs_0(_field.Fields, _option.SdefOption):
    """
    Represents INP `axs` elements variation #0.
    """

    _KEYWORD = 'axs'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    x = _field.Field(types.Real, 'Reference vector for EXT and RAD x-component', required=True)
    y = _field.Field(types.Real, 'Reference vector for EXT and RAD y-component', required=True)
    z = _field.Field(types.Real, 'Reference vector for EXT and RAD z-component', required=True)

    _REGEX = re.compile(rf'\Aaxs( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
