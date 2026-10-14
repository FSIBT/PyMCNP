import re

from .. import _field
from . import _option
from ... import errors


class Printal(_field.Fields, _option.MplotOption):
    """
    Represents INP `printal` elements.
    """

    _CODE = errors.InpCode.SEMANTICS_CARD

    _KEYWORD = 'printal'

    _REGEX = re.compile(r'\Aprintal\Z', re.IGNORECASE)
