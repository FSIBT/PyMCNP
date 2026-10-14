import re

from .. import _field
from . import _option
from ... import types


class Iso(_field.Fields, _option.KsenOption):
    """
    Represents INP `iso` elements.
    """

    _KEYWORD = 'iso'

    zaids = _field.Field.tuple(types.Zaid, 'List of ZAIDs for pertubation', required=True, numeric=())

    _REGEX = re.compile(rf'\Aiso((?: {types.Zaid._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
