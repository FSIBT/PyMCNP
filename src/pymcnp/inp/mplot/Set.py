import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Set(_field.Fields, _option.MplotOption):
    """
    Represents INP `set` elements.
    """

    _KEYWORD = 'set'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    f = _field.Field(types.Integer, 'F bin number', required=True, numeric=int)
    d = _field.Field(types.Integer, 'D bin number', required=True, numeric=int)
    u = _field.Field(types.Integer, 'U bin number', required=True, numeric=int)
    s = _field.Field(types.Integer, 'S bin number', required=True, numeric=int)
    m = _field.Field(types.Integer, 'M bin number', required=True, numeric=int)
    c = _field.Field(types.Integer, 'C bin number', required=True, numeric=int)
    e = _field.Field(types.Integer, 'E bin number', required=True, numeric=int)
    t = _field.Field(types.Integer, 'T bin number', required=True, numeric=int)

    _REGEX = re.compile(
        rf'\Aset( {types.Integer._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})\Z',
        re.IGNORECASE,
    )
