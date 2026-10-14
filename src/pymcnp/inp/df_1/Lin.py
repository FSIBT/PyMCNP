import re

from .. import _field
from . import _option


class Lin(_field.Fields, _option.DfOption_1):
    """
    Represents INP `lin` elements.
    """

    _KEYWORD = 'lin'

    _REGEX = re.compile(r'\Alin\Z', re.IGNORECASE)
