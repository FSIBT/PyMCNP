import re

from ... import _field
from . import _option


class Pct(_field.Fields, _option.ContourOption):
    """
    Represents INP `pct` elements.
    """

    _KEYWORD = 'pct'

    _REGEX = re.compile(r'\Apct\Z', re.IGNORECASE)
