import re

from .. import _field
from . import _option
from ... import types


class Conic(_field.Fields, _option.PtracOption):
    """
    Represents INP `conic` elements.
    """

    _KEYWORD = 'conic'

    setting = _field.Field(
        types.String, 'Activates a PTRAC file format specifically for coincidence tally scoring', required=True, numeric=(), invalid=lambda self, value: value.value.lower() not in {'col', 'lin'}
    )

    _REGEX = re.compile(r'\Aconic(?: (col|lin))\Z', re.IGNORECASE)
