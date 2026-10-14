import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Hstep(_field.Fields, _option.MOption_0):
    """
    Represents INP `hstep` elements.
    """

    _KEYWORD = 'hstep'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    step = _field.Field(types.Integer, 'Number of proton sub-step per energy step', required=True, numeric=int, invalid=lambda self, value: not value >= 0)

    _REGEX = re.compile(rf'\Ahstep( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
