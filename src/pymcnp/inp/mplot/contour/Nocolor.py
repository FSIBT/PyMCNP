import re

from ... import _field
from . import _option
from .... import errors


class Nocolor(_field.Fields, _option.ContourOption):
    """
    Represents INP `nocolor` elements.
    """

    _CODE = errors.InpCode.SEMANTICS_CARD

    _KEYWORD = 'nocolor'

    _REGEX = re.compile(r'\Anocolor\Z', re.IGNORECASE)
