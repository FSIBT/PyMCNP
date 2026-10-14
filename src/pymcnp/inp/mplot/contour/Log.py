import re

from ... import _field
from . import _option
from .... import errors


class Log(_field.Fields, _option.ContourOption):
    """
    Represents INP `log` elements.
    """

    _CODE = errors.InpCode.SEMANTICS_CARD

    _KEYWORD = 'log'

    _REGEX = re.compile(r'\Alog\Z', re.IGNORECASE)
