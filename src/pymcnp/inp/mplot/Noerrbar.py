import re

from .. import _field
from . import _option


class Noerrbar(_field.Fields, _option.MplotOption):
    """
    Represents INP `noerrbar` elements.
    """

    _KEYWORD = 'noerrbar'

    _REGEX = re.compile(r'\Anoerrbar\Z', re.IGNORECASE)
