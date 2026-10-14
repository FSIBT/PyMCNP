import re

from .. import _field
from . import _option
from ... import errors


class Help(_field.Fields, _option.MplotOption):
    """
    Represents INP `help` elements.
    """

    _CODE = errors.InpCode.SEMANTICS_CARD

    _KEYWORD = 'help'

    _REGEX = re.compile(r'\Ahelp\Z', re.IGNORECASE)
