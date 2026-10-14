import re

from ... import _field
from . import _option
from .... import errors


class Noline(_field.Fields, _option.ContourOption):
    """
    Represents INP `noline` elements.
    """

    _CODE = errors.InpCode.SEMANTICS_CARD

    _KEYWORD = 'noline'

    _REGEX = re.compile(r'\Anoline\Z', re.IGNORECASE)
