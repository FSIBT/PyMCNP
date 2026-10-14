import re

from ... import _field
from . import _option


class Noline(_field.Fields, _option.ContourOption):
    """
    Represents INP `noline` elements.
    """

    _KEYWORD = 'noline'

    _REGEX = re.compile(r'\Anoline\Z', re.IGNORECASE)
