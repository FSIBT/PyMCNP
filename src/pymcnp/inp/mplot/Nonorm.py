import re

from .. import _field
from . import _option


class Nonorm(_field.Fields, _option.MplotOption):
    """
    Represents INP `nonorm` elements.
    """

    _KEYWORD = 'nonorm'

    _REGEX = re.compile(r'\Anonorm\Z', re.IGNORECASE)
