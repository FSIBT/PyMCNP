import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Y_0(_field.Fields, _option.SdefOption):
    """
    Represents INP `y` elements variation #0.
    """

    _KEYWORD = 'y'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    position = _field.Field(types.Real, 'Position y-component', required=True)

    _REGEX = re.compile(rf'\Ay( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
