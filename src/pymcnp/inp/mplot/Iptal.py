import re

from .. import _field
from . import _option


class Iptal(_field.Fields, _option.MplotOption):
    """
    Represents INP `iptal` elements.
    """

    _KEYWORD = 'iptal'

    _REGEX = re.compile(r'\Aiptal\Z', re.IGNORECASE)
