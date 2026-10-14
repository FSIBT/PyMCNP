import re

from .. import _field
from . import _option


class Hist(_field.Fields, _option.MplotOption):
    """
    Represents INP `hist` elements.
    """

    _KEYWORD = 'hist'

    _REGEX = re.compile(r'\Ahist\Z', re.IGNORECASE)
