import re

from .. import _field
from . import _option
from ... import errors


class Coplot(_field.Fields, _option.MplotOption):
    """
    Represents INP `coplot` elements.
    """

    _CODE = errors.InpCode.SEMANTICS_CARD

    _KEYWORD = 'coplot'

    _REGEX = re.compile(r'\Acoplot\Z', re.IGNORECASE)
