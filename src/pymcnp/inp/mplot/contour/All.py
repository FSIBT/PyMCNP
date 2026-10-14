import re

from ... import _field
from . import _option


class All(_field.Fields, _option.ContourOption):
    """
    Represents INP `all` elements.
    """

    _KEYWORD = 'all'

    _REGEX = re.compile(r'\Aall\Z', re.IGNORECASE)
