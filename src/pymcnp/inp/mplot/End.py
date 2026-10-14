import re

from .. import _field
from . import _option
from ... import errors


class End(_field.Fields, _option.MplotOption):
    """
    Represents INP `end` elements.
    """

    _CODE = errors.InpCode.SEMANTICS_CARD

    _KEYWORD = 'end'

    _REGEX = re.compile(r'\Aend\Z', re.IGNORECASE)
