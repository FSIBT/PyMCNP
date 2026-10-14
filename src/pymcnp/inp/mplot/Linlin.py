import re

from .. import _field
from . import _option


class Linlin(_field.Fields, _option.MplotOption):
    """
    Represents INP `linlin` elements.
    """

    _KEYWORD = 'linlin'

    _REGEX = re.compile(r'\Alinlin\Z', re.IGNORECASE)
