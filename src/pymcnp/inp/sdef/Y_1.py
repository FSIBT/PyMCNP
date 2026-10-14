import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Y_1(_field.Fields, _option.SdefOption):
    """
    Represents INP `y` elements variation #1.
    """

    _KEYWORD = 'y'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    position = _field.Field(types.Distribution, 'Position y-component', required=True, numeric=())

    _REGEX = re.compile(rf'\Ay( {types.Distribution._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
