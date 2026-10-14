import re

from .. import _field
from . import _option


class Log(_field.Fields, _option.DfOption_1):
    """
    Represents INP `log` elements.
    """

    _KEYWORD = 'log'

    _REGEX = re.compile(r'\Alog\Z', re.IGNORECASE)
