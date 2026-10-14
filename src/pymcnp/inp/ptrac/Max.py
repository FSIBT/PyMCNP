import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Max(_field.Fields, _option.PtracOption):
    """
    Represents INP `max` elements.
    """

    _KEYWORD = 'max'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    events = _field.Field(types.Integer, 'Maximum number of events to write', required=True, numeric=int, invalid=lambda self, value: not value != 0)

    _REGEX = re.compile(rf'\Amax( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
