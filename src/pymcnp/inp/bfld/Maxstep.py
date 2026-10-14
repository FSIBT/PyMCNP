import re

from .. import _field
from . import _option
from ... import types


class Maxstep(_field.Fields, _option.BfldOption):
    """
    Represents INP `maxstep` elements.
    """

    _KEYWORD = 'maxstep'

    size = _field.Field(types.Real, 'Maximum step size', required=True)

    _REGEX = re.compile(rf'\Amaxstep( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
