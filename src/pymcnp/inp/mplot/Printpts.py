import re

from .. import _field
from . import _option
from ... import errors


class Printpts(_field.Fields, _option.MplotOption):
    """
    Represents INP `printpts` elements.
    """

    _CODE = errors.InpCode.SEMANTICS_CARD

    _KEYWORD = 'printpts'

    _REGEX = re.compile(r'\Aprintpts\Z', re.IGNORECASE)
