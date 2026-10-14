import re

from .. import _field
from . import _option


class Loglin(_field.Fields, _option.MplotOption):
    """
    Represents INP `loglin` elements.
    """

    _KEYWORD = 'loglin'

    _REGEX = re.compile(r'\Aloglin\Z', re.IGNORECASE)
