import re

from .. import _field
from . import _option


class Lethargy(_field.Fields, _option.MplotOption):
    """
    Represents INP `lethargy` elements.
    """

    _KEYWORD = 'lethargy'

    _REGEX = re.compile(r'\Alethargy\Z', re.IGNORECASE)
