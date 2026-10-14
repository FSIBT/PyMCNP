import re

from .. import _field
from . import _option
from ... import errors


class Noerrbar(_field.Fields, _option.MplotOption):
    """
    Represents INP `noerrbar` elements.
    """

    _CODE = errors.InpCode.SEMANTICS_CARD

    _KEYWORD = 'noerrbar'

    _REGEX = re.compile(r'\Anoerrbar\Z', re.IGNORECASE)
