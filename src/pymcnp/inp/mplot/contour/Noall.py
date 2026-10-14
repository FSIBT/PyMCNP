import re

from ... import _field
from . import _option


class Noall(_field.Fields, _option.ContourOption):
    """
    Represents INP `noall` elements.
    """

    _KEYWORD = 'noall'

    _REGEX = re.compile(r'\Anoall\Z', re.IGNORECASE)
