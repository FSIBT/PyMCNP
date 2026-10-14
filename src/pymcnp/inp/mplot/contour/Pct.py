import re

from ... import _field
from . import _option
from .... import errors


class Pct(_field.Fields, _option.ContourOption):
    """
    Represents INP `pct` elements.
    """

    _CODE = errors.InpCode.SEMANTICS_CARD

    _KEYWORD = 'pct'

    _REGEX = re.compile(r'\Apct\Z', re.IGNORECASE)
