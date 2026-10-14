import re

from .. import _field
from . import _option
from ... import types


class List(_field.Fields, _option.EmbeeOption):
    """
    Represents INP `list` elements.
    """

    _KEYWORD = 'list'

    reactions = _field.Field(types.Real, 'List of reactions', required=True)

    _REGEX = re.compile(rf'\Alist( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
