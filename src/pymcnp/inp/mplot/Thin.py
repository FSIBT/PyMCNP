import re

from .. import _field
from . import _option
from ... import errors


class Thin(_field.Fields, _option.MplotOption):
    """
    Represents INP `thin` elements.
    """

    _CODE = errors.InpCode.SEMANTICS_CARD

    _KEYWORD = 'thin'

    _REGEX = re.compile(r'\Athin\Z', re.IGNORECASE)
