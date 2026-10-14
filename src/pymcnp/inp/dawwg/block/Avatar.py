import re

from ... import _field
from . import _option
from .... import types


class Avatar(_field.Fields, _option.BlockOption):
    """
    Represents INP `avatar` elements.
    """

    _KEYWORD = 'avatar'

    setting = _field.Field(types.Integer, 'Prepare special XMFLUXA file on/off', required=True, numeric=int, invalid=lambda self, value: value not in {0, 1})

    _REGEX = re.compile(rf'\Aavatar( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
