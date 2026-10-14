import re

from .. import _field
from . import _option
from ... import errors


class Below(_field.Fields, _option.MplotOption):
    """
    Represents INP `below` elements.
    """

    _CODE = errors.InpCode.SEMANTICS_CARD

    _KEYWORD = 'below'

    _REGEX = re.compile(r'\Abelow\Z', re.IGNORECASE)
