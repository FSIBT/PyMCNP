import re

from ... import _field
from . import _option


class Lin(_field.Fields, _option.ContourOption):
    """
    Represents INP `lin` elements.
    """

    _KEYWORD = 'lin'

    _REGEX = re.compile(r'\Alin\Z', re.IGNORECASE)
