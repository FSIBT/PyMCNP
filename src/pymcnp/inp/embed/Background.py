import re

from .. import _field
from . import _option
from ... import types


class Background(_field.Fields, _option.EmbedOption):
    """
    Represents INP `background` elements.
    """

    _KEYWORD = 'background'

    number = _field.Field(types.Integer, 'Background pseudo-cell number', required=True, numeric=int, invalid=lambda self, value: not (value >= 1 and value <= 99999999))

    _REGEX = re.compile(rf'\Abackground( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
