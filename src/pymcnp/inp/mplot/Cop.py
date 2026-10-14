import re

from .. import _field
from . import _option


class Cop(_field.Fields, _option.MplotOption):
    """
    Represents INP `cop` elements.
    """

    _KEYWORD = 'cop'

    _REGEX = re.compile(r'\Acop\Z', re.IGNORECASE)
