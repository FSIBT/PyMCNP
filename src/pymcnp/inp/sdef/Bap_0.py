import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Bap_0(_field.Fields, _option.SdefOption):
    """
    Represents INP `bap` elements variation #0.
    """

    _KEYWORD = 'bap'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    ba1 = _field.Field(types.Real, 'Beam aperture half-width in the x transverse direction', required=True)
    ba2 = _field.Field(types.Real, 'Beam aperture half-width in the y transverse direction', required=True)
    u = _field.Field(types.Real, 'Unused, arrbirary value', required=True)

    _REGEX = re.compile(rf'\Abap( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
