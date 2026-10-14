import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Thick(_field.Fields, _option.MplotOption):
    """
    Represents INP `thick` elements.
    """

    _KEYWORD = 'thick'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    x = _field.Field(types.Real, 'Thickness of plot curves', required=True)

    _REGEX = re.compile(rf'\Athick( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
