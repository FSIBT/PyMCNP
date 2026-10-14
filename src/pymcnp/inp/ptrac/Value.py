import re

from .. import _field
from . import _option
from ... import types


class Value(_field.Fields, _option.PtracOption):
    """
    Represents INP `value` elements.
    """

    _KEYWORD = 'value'

    cutoff = _field.Field(types.Real, 'Specifies tally cutoff above which history events will be written', required=True)

    _REGEX = re.compile(rf'\Avalue( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
