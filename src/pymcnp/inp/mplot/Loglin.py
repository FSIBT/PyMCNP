import re

from .. import _field
from . import _option
from ... import errors


class Loglin(_field.Fields, _option.MplotOption):
    """
    Represents INP `loglin` elements.
    """

    _CODE = errors.InpCode.SEMANTICS_CARD

    _KEYWORD = 'loglin'

    _REGEX = re.compile(r'\Aloglin\Z', re.IGNORECASE)
