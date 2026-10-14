import re

from ... import _field
from . import _option
from .... import errors


class Line(_field.Fields, _option.ContourOption):
    """
    Represents INP `line` elements.
    """

    _CODE = errors.InpCode.SEMANTICS_CARD

    _KEYWORD = 'line'

    _REGEX = re.compile(r'\Aline\Z', re.IGNORECASE)
