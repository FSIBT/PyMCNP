import re

from .. import _field
from . import _option


class Plinear(_field.Fields, _option.MplotOption):
    """
    Represents INP `plinear` elements.
    """

    _KEYWORD = 'plinear'

    _REGEX = re.compile(r'\Aplinear\Z', re.IGNORECASE)
