import re

from .. import _field
from . import _option


class Bar(_field.Fields, _option.MplotOption):
    """
    Represents INP `bar` elements.
    """

    _KEYWORD = 'bar'

    _REGEX = re.compile(r'\Abar\Z', re.IGNORECASE)
