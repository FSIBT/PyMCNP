import re

from .. import _field
from . import _option
from ... import errors


class Bar(_field.Fields, _option.MplotOption):
    """
    Represents INP `bar` elements.
    """

    _CODE = errors.InpCode.SEMANTICS_CARD

    _KEYWORD = 'bar'

    _REGEX = re.compile(r'\Abar\Z', re.IGNORECASE)
