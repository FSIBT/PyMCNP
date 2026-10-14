import re

from .. import _field
from . import _option


class Printpts(_field.Fields, _option.MplotOption):
    """
    Represents INP `printpts` elements.
    """

    _KEYWORD = 'printpts'

    _REGEX = re.compile(r'\Aprintpts\Z', re.IGNORECASE)
