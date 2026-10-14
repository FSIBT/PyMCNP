import re

from .. import _field
from . import _option
from ... import errors


class Cop(_field.Fields, _option.MplotOption):
    """
    Represents INP `cop` elements.
    """

    _CODE = errors.InpCode.SEMANTICS_CARD

    _KEYWORD = 'cop'

    _REGEX = re.compile(r'\Acop\Z', re.IGNORECASE)
