import re

from .. import _field
from . import _option


class End(_field.Fields, _option.MplotOption):
    """
    Represents INP `end` elements.
    """

    _KEYWORD = 'end'

    _REGEX = re.compile(r'\Aend\Z', re.IGNORECASE)
