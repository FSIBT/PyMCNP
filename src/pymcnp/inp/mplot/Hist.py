import re

from .. import _field
from . import _option
from ... import errors


class Hist(_field.Fields, _option.MplotOption):
    """
    Represents INP `hist` elements.
    """

    _CODE = errors.InpCode.SEMANTICS_CARD

    _KEYWORD = 'hist'

    _REGEX = re.compile(r'\Ahist\Z', re.IGNORECASE)
