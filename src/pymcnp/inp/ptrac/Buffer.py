import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Buffer(_field.Fields, _option.PtracOption):
    """
    Represents INP `buffer` elements.
    """

    _KEYWORD = 'buffer'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    storage = _field.Field(types.Integer, 'Amount of storage available for filtered events', required=True, numeric=int, invalid=lambda self, value: not value > 0)

    _REGEX = re.compile(rf'\Abuffer( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
