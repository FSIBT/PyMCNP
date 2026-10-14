import re

from .. import _field
from . import _option
from ... import errors


class Linlin(_field.Fields, _option.MplotOption):
    """
    Represents INP `linlin` elements.
    """

    _CODE = errors.InpCode.SEMANTICS_CARD

    _KEYWORD = 'linlin'

    _REGEX = re.compile(r'\Alinlin\Z', re.IGNORECASE)
