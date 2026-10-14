import re

from .. import _field
from . import _option


class Linlog(_field.Fields, _option.MplotOption):
    """
    Represents INP `linlog` elements.
    """

    _KEYWORD = 'linlog'

    _REGEX = re.compile(r'\Alinlog\Z', re.IGNORECASE)
