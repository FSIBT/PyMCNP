import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Iso(_field.Fields, _option.KpertOption):
    """
    Represents INP `iso` elements.
    """

    _KEYWORD = 'iso'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    zaids = _field.Field.tuple(types.Zaid, 'List of ZAIDs for pertubation', required=True, numeric=())

    _REGEX = re.compile(rf'\Aiso((?: {types.Zaid._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
