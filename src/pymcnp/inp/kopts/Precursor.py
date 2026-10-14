import re

from .. import _field
from . import _option
from ... import types


class Precursor(_field.Fields, _option.KoptsOption):
    """
    Represents INP `precursor` elements.
    """

    _KEYWORD = 'precursor'

    setting = _field.Field(types.String, 'Yes/No detailed precursor information', required=True, numeric=(), invalid=lambda self, value: value.value.lower() not in {'yes', 'no'})

    _REGEX = re.compile(rf'\Aprecursor( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
