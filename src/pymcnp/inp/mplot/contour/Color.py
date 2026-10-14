import re

from ... import _field
from . import _option
from .... import errors


class Color(_field.Fields, _option.ContourOption):
    """
    Represents INP `color` elements.
    """

    _CODE = errors.InpCode.SEMANTICS_CARD

    _KEYWORD = 'color'

    _REGEX = re.compile(r'\Acolor\Z', re.IGNORECASE)
