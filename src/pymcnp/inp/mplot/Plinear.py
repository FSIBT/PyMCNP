import re

from .. import _field
from . import _option
from ... import errors


class Plinear(_field.Fields, _option.MplotOption):
    """
    Represents INP `plinear` elements.
    """

    _CODE = errors.InpCode.SEMANTICS_CARD

    _KEYWORD = 'plinear'

    _REGEX = re.compile(r'\Aplinear\Z', re.IGNORECASE)
