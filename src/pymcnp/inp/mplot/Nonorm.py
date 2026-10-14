import re

from .. import _field
from . import _option
from ... import errors


class Nonorm(_field.Fields, _option.MplotOption):
    """
    Represents INP `nonorm` elements.
    """

    _CODE = errors.InpCode.SEMANTICS_CARD

    _KEYWORD = 'nonorm'

    _REGEX = re.compile(r'\Anonorm\Z', re.IGNORECASE)
