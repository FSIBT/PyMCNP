import re

from .. import _field
from . import _option


class Help(_field.Fields, _option.MplotOption):
    """
    Represents INP `help` elements.
    """

    _KEYWORD = 'help'

    _REGEX = re.compile(r'\Ahelp\Z', re.IGNORECASE)
