import re

from ... import _field
from . import _option
from .... import errors


class Noall(_field.Fields, _option.FreeOption):
    """
    Represents INP `noall` elements.
    """

    _CODE = errors.InpCode.SEMANTICS_CARD

    _KEYWORD = 'noall'

    _REGEX = re.compile(r'\Anoall\Z', re.IGNORECASE)
