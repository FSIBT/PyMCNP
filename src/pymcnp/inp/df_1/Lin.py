import re

from .. import _field
from . import _option
from ... import errors


class Lin(_field.Fields, _option.DfOption_1):
    """
    Represents INP `lin` elements.
    """

    _CODE = errors.InpCode.SEMANTICS_CARD

    _KEYWORD = 'lin'

    _REGEX = re.compile(r'\Alin\Z', re.IGNORECASE)
