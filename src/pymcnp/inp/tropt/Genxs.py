import re

from .. import _field
from . import _option
from ... import types


class Genxs(_field.Fields, _option.TroptOption):
    """
    Represents INP `genxs` elements.
    """

    _KEYWORD = 'genxs'

    filename = _field.Field(types.String, 'Cross section generation setting', numeric=())

    _REGEX = re.compile(rf'\Agenxs( {types.String._REGEX.pattern[2:-2]})?\Z', re.IGNORECASE)
