import re

from .. import _field
from . import _option


class Below(_field.Fields, _option.MplotOption):
    """
    Represents INP `below` elements.
    """

    _KEYWORD = 'below'

    _REGEX = re.compile(r'\Abelow\Z', re.IGNORECASE)
