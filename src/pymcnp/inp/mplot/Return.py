import re

from .. import _field
from . import _option


class Return(_field.Fields, _option.MplotOption):
    """
    Represents INP `return` elements.
    """

    _KEYWORD = 'return'

    _REGEX = re.compile(r'\Areturn\Z', re.IGNORECASE)
