import re

from ... import _field
from . import _option


class Color(_field.Fields, _option.ContourOption):
    """
    Represents INP `color` elements.
    """

    _KEYWORD = 'color'

    _REGEX = re.compile(r'\Acolor\Z', re.IGNORECASE)
