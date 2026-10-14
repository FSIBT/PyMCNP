import re

from .. import _field
from . import _option
from ... import errors


class Iptal(_field.Fields, _option.MplotOption):
    """
    Represents INP `iptal` elements.
    """

    _CODE = errors.InpCode.SEMANTICS_CARD

    _KEYWORD = 'iptal'

    _REGEX = re.compile(r'\Aiptal\Z', re.IGNORECASE)
