import re

from .. import _field
from . import _option


class Status(_field.Fields, _option.MplotOption):
    """
    Represents INP `status` elements.
    """

    _KEYWORD = 'status'

    _REGEX = re.compile(r'\Astatus\Z', re.IGNORECASE)
