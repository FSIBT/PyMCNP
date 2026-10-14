import re

from .. import _field
from . import _option
from ... import errors


class Linlog(_field.Fields, _option.MplotOption):
    """
    Represents INP `linlog` elements.
    """

    _CODE = errors.InpCode.SEMANTICS_CARD

    _KEYWORD = 'linlog'

    _REGEX = re.compile(r'\Alinlog\Z', re.IGNORECASE)
