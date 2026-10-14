import re

from .. import _field
from . import _option
from ... import errors


class Options(_field.Fields, _option.MplotOption):
    """
    Represents INP `options` elements.
    """

    _CODE = errors.InpCode.SEMANTICS_CARD

    _KEYWORD = 'options'

    _REGEX = re.compile(r'\Aoptions\Z', re.IGNORECASE)
