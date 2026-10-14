import re

from .. import _field
from . import _option
from ... import types


class Fixed(_field.Fields, _option.MplotOption):
    """
    Represents INP `fixed` elements.
    """

    _KEYWORD = 'fixed'

    q = _field.Field(types.String, 'Fixed variable', required=True, numeric=(), invalid=lambda self, value: value.value.lower() not in {'f', 'd', 'u', 's', 'm', 'c', 'e', 't', 'i', 'j', 'k'})
    n = _field.Field(types.Integer, 'Bin number', required=True, numeric=int)

    _REGEX = re.compile(rf'\Afixed( {types.String._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
