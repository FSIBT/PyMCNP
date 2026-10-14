import re

from .. import _field
from . import _option
from ... import errors


class Return(_field.Fields, _option.MplotOption):
    """
    Represents INP `return` elements.
    """

    _CODE = errors.InpCode.SEMANTICS_CARD

    _KEYWORD = 'return'

    _REGEX = re.compile(r'\Areturn\Z', re.IGNORECASE)
