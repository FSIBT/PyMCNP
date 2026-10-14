import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Dnbais(_field.Fields, _option.ActOption):
    """
    Represents INP `dnbais` elements.
    """

    _KEYWORD = 'dnbais'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    count = _field.Field(types.Integer, 'Maximum number of neutrons generated per reaction', required=True, numeric=int, invalid=lambda self, value: not (value >= 0 and value <= 10))

    _REGEX = re.compile(rf'\Adnbais( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
