import re

from . import _field
from . import _card
from .. import types


class Tr_1(_field.Fields, _card.Card):
    """
    Represents INP `tr` elements variation #1.
    """

    _KEYWORD = 'tr'

    _ORDER = ('suffix', 'x', 'y', 'z', 'xx', 'xy', 'xz', 'yx', 'yy', 'yz', 'prefix', 'system')

    prefix = _field.Field(types.String, 'Star prefix', numeric=(), invalid=lambda self, value: value is not None and value.value.lower() not in {'*'})
    suffix = _field.Field(types.Integer, 'Data card option suffix', required=True, numeric=int, invalid=lambda self, value: not (value >= 1 and value <= 999))
    x = _field.Field(types.Real, 'Displacement vector x component', required=True)
    y = _field.Field(types.Real, 'Displacement vector y component', required=True)
    z = _field.Field(types.Real, 'Displacement vector z component', required=True)
    xx = _field.Field(types.Real, "Rotation matrix xx' component", required=True)
    xy = _field.Field(types.Real, "Rotation matrix xy' component", required=True)
    xz = _field.Field(types.Real, "Rotation matrix xz' component", required=True)
    yx = _field.Field(types.Real, "Rotation matrix yx' component", required=True)
    yy = _field.Field(types.Real, "Rotation matrix yy' component", required=True)
    yz = _field.Field(types.Real, "Rotation matrix yz' component", required=True)
    system = _field.Field(types.Integer, 'Coordinate system setting', numeric=int, invalid=lambda self, value: value is not None and (not (value == -1 or value == 1)))

    _REGEX = re.compile(
        rf'\A([*])?tr(\d+)( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})?\Z',
        re.IGNORECASE,
    )
