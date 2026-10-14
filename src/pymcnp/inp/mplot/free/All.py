import re

from ... import _field
from . import _option
from .... import errors


class All(_field.Fields, _option.FreeOption):
    """
    Represents INP `all` elements.
    """

    _CODE = errors.InpCode.SEMANTICS_CARD

    _KEYWORD = 'all'

    _REGEX = re.compile(r'\Aall\Z', re.IGNORECASE)
