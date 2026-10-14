import re

from .. import _field
from . import _option
from ... import types


class Ksental(_field.Fields, _option.KoptsOption):
    """
    Represents INP `ksental` elements.
    """

    _KEYWORD = 'ksental'

    fileopt = _field.Field(types.String, 'Format of sensity profiles output file', required=True, numeric=(), invalid=lambda self, value: value.value.lower() not in {'mctal', 'tsunami-b'})

    _REGEX = re.compile(rf'\Aksental( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
