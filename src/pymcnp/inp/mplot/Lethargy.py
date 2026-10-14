import re

from .. import _field
from . import _option
from ... import errors


class Lethargy(_field.Fields, _option.MplotOption):
    """
    Represents INP `lethargy` elements.
    """

    _CODE = errors.InpCode.SEMANTICS_CARD

    _KEYWORD = 'lethargy'

    _REGEX = re.compile(r'\Alethargy\Z', re.IGNORECASE)
