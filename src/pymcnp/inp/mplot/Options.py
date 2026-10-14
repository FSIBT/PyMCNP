import re

from .. import _field
from . import _option


class Options(_field.Fields, _option.MplotOption):
    """
    Represents INP `options` elements.
    """

    _KEYWORD = 'options'

    _REGEX = re.compile(r'\Aoptions\Z', re.IGNORECASE)
