import re

from . import _field
from . import _card
from .. import types


class Fir(_field.Fields, _card.Card):
    """
    Represents INP `fir` cards.
    """

    _KEYWORD = 'fir'

    _ORDER = ('suffix', 'x1', 'y1', 'z1', 'ro', 'x2', 'y2', 'z2', 'f1', 'f2', 'f3', 'designator')

    suffix = _field.Field(types.Integer, 'Data card option suffix', required=True, numeric=int, invalid=lambda self, value: not (value <= 99999999 and value % 10 == 5))
    designator = _field.Field(types.Designator, 'Data card particle designator', numeric=())
    x1 = _field.Field(types.Real, 'Rectangular grid center x-coordinate', required=True)
    y1 = _field.Field(types.Real, 'Rectangular grid center y-coordinate', required=True)
    z1 = _field.Field(types.Real, 'Rectangular grid center z-coordinate', required=True)
    ro = _field.Field(types.Real, 'Rectangular grid exclusion radius', required=True, invalid=lambda self, value: not value == 0)
    x2 = _field.Field(types.Real, 'Reference direction x-coordinate', required=True)
    y2 = _field.Field(types.Real, 'Reference direction y-coordinate', required=True)
    z2 = _field.Field(types.Real, 'Reference direction z-coordinate', required=True)
    f1 = _field.Field(types.Real, 'Source contributions on/off', required=True, invalid=lambda self, value: value not in {0, -1, 1})
    f2 = _field.Field(types.Real, 'Radial view of field', required=True)
    f3 = _field.Field(types.Real, 'Contribution offset setting', required=True, invalid=lambda self, value: value not in {0, -1, 1})

    _REGEX = re.compile(
        rf'\Afir(\d+)(?::(\S+))?( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z',
        re.IGNORECASE,
    )
