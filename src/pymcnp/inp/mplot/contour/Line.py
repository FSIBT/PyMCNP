import re

from ... import _field
from . import _option


class Line(_field.Fields, _option.ContourOption):
    """
    Represents INP `line` elements.
    """

    _KEYWORD = 'line'

    _REGEX = re.compile(r'\Aline\Z', re.IGNORECASE)
