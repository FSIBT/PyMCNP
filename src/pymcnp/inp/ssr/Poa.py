import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Poa(_field.Fields, _option.SsrOption):
    """
    Represents INP `poa` elements.
    """

    _KEYWORD = 'poa'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    angle = _field.Field(types.Real, 'Angle within which particles accepeted for transport', required=True)

    _REGEX = re.compile(rf'\Apoa( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
