import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Ext_0(_field.Fields, _option.SdefOption):
    """
    Represents INP `ext` elements variation #0.
    """

    _KEYWORD = 'ext'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    distance_cosine = _field.Field(types.Real, 'Distance for POS along AXS or Cosine of angle from AXS', required=True)

    _REGEX = re.compile(rf'\Aext( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
