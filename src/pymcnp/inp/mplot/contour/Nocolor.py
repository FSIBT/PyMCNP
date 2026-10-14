import re

from ... import _field
from . import _option


class Nocolor(_field.Fields, _option.ContourOption):
    """
    Represents INP `nocolor` elements.
    """

    _KEYWORD = 'nocolor'

    _REGEX = re.compile(r'\Anocolor\Z', re.IGNORECASE)
