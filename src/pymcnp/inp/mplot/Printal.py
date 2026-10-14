import re

from .. import _field
from . import _option


class Printal(_field.Fields, _option.MplotOption):
    """
    Represents INP `printal` elements.
    """

    _KEYWORD = 'printal'

    _REGEX = re.compile(r'\Aprintal\Z', re.IGNORECASE)
