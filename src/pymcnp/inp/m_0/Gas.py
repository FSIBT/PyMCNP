import re

from .. import _field
from . import _option
from ... import types


class Gas(_field.Fields, _option.MOption_0):
    """
    Represents INP `gas` elements.
    """

    _KEYWORD = 'gas'

    setting = _field.Field(
        types.String, 'Flag for density-effect correction to electron stopping power', required=True, numeric=(), invalid=lambda self, value: value.value.lower() not in {'yes', 'no'}
    )

    _REGEX = re.compile(rf'\Agas( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
