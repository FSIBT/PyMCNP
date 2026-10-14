import re

from .. import _field
from . import free
from . import _option
from ... import types


class Free(_field.Fields, _option.MplotOption):
    """
    Represents INP `free` elements.
    """

    _KEYWORD = 'free'

    x = _field.Field(types.String, 'Independent variable', required=True, numeric=(), invalid=lambda self, value: value.value.lower() not in {'f', 'd', 'u', 's', 'm', 'c', 'e', 't', 'i', 'j', 'k'})
    y = _field.Field(types.String, 'Dependent variable', required=True, numeric=(), invalid=lambda self, value: value.value.lower() not in {'f', 'd', 'u', 's', 'm', 'c', 'e', 't', 'i', 'j', 'k'})
    option = _field.Field(free.FreeOption, 'Free option', numeric=())

    _REGEX = re.compile(rf'\Afree( {types.String._REGEX.pattern[2:-2]})( {types.String._REGEX.pattern[2:-2]})( (?:{free.FreeOption._REGEX.pattern[2:-2]}))?\Z', re.IGNORECASE)
