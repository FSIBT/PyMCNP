import re

from .. import _field
from . import _option


class Coplot(_field.Fields, _option.MplotOption):
    """
    Represents INP `coplot` elements.
    """

    _KEYWORD = 'coplot'

    _REGEX = re.compile(r'\Acoplot\Z', re.IGNORECASE)
