import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Fill_0(_field.Fields, _option.CellOption):
    """
    Represents INP `fill` elements variation #0.
    """

    _KEYWORD = 'fill'

    _CODE = errors.InpCode.SEMANTICS_OPTION
    _ORDER = ('i', 'j', 'k', 'universes', 'prefix', 'm')

    prefix = _field.Field(types.String, 'Star prefix', numeric=(), invalid=lambda self, value: value is not None and value.value.lower() not in {'*'})
    i = _field.Field(types.Index, 'Lattice parameter #1', required=True, numeric=())
    j = _field.Field(types.Index, 'Lattice parameter #2', required=True, numeric=())
    k = _field.Field(types.Index, 'Lattice parameter #3', required=True, numeric=())
    universes = _field.Field.tuple(types.Integer, 'Fill universe numbers', required=True, numeric=int)
    m = _field.Field(types.Integer, 'Displacement vector origin', numeric=int)

    _REGEX = re.compile(rf'\A([*])?fill (\S+:\S+) (\S+:\S+) (\S+:\S+)((?: {types.Integer._REGEX.pattern[2:-2]})+?)(?: [(]({types.Integer._REGEX.pattern[2:-2]})[)])?\Z', re.IGNORECASE)
