import re

from .. import _field
from . import _option


class Thin(_field.Fields, _option.MplotOption):
    """
    Represents INP `thin` elements.
    """

    _KEYWORD = 'thin'

    _REGEX = re.compile(r'\Athin\Z', re.IGNORECASE)
