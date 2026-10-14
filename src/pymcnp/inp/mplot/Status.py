import re

from .. import _field
from . import _option
from ... import errors


class Status(_field.Fields, _option.MplotOption):
    """
    Represents INP `status` elements.
    """

    _CODE = errors.InpCode.SEMANTICS_CARD

    _KEYWORD = 'status'

    _REGEX = re.compile(r'\Astatus\Z', re.IGNORECASE)
