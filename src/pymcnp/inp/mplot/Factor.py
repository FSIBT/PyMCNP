import re

from .. import _field
from . import _option
from ... import types


class Factor(_field.Fields, _option.MplotOption):
    """
    Represents INP `factor` elements.
    """

    _KEYWORD = 'factor'

    a = _field.Field(types.String, 'Multiplication axis', required=True, numeric=(), invalid=lambda self, value: value.value.lower() not in {'x', 'y', 'z'})
    f = _field.Field(types.Real, 'Multiplication factor', required=True)
    s = _field.Field(types.Real, 'Addative term')

    _REGEX = re.compile(rf'\Afactor( {types.String._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})?\Z', re.IGNORECASE)
