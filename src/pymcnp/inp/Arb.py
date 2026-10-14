import re

from . import _field
from . import _surface
from .. import types
from .. import errors


class Arb(_surface.Surface):
    """
    Represents INP `arb` surface cards.
    """

    _KEYWORD = 'arb'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    ax = _field.Field(types.Real, 'Polyhedron corner #1 x component', required=True)
    ay = _field.Field(types.Real, 'Polyhedron corner #1 y component', required=True)
    az = _field.Field(types.Real, 'Polyhedron corner #1 z component', required=True)
    bx = _field.Field(types.Real, 'Polyhedron corner #2 x component', required=True)
    by = _field.Field(types.Real, 'Polyhedron corner #2 y component', required=True)
    bz = _field.Field(types.Real, 'Polyhedron corner #2 z component', required=True)
    cx = _field.Field(types.Real, 'Polyhedron corner #3 x component', required=True)
    cy = _field.Field(types.Real, 'Polyhedron corner #3 y component', required=True)
    cz = _field.Field(types.Real, 'Polyhedron corner #3 z component', required=True)
    dx = _field.Field(types.Real, 'Polyhedron corner #4 x component', required=True)
    dy = _field.Field(types.Real, 'Polyhedron corner #4 y component', required=True)
    dz = _field.Field(types.Real, 'Polyhedron corner #4 z component', required=True)
    ex = _field.Field(types.Real, 'Polyhedron corner #5 x component', required=True)
    ey = _field.Field(types.Real, 'Polyhedron corner #5 y component', required=True)
    ez = _field.Field(types.Real, 'Polyhedron corner #5 z component', required=True)
    fx = _field.Field(types.Real, 'Polyhedron corner #6 x component', required=True)
    fy = _field.Field(types.Real, 'Polyhedron corner #6 y component', required=True)
    fz = _field.Field(types.Real, 'Polyhedron corner #6 z component', required=True)
    gx = _field.Field(types.Real, 'Polyhedron corner #7 x component', required=True)
    gy = _field.Field(types.Real, 'Polyhedron corner #7 y component', required=True)
    gz = _field.Field(types.Real, 'Polyhedron corner #7 z component', required=True)
    hx = _field.Field(types.Real, 'Polyhedron corner #8 x component', required=True)
    hy = _field.Field(types.Real, 'Polyhedron corner #8 y component', required=True)
    hz = _field.Field(types.Real, 'Polyhedron corner #8 z component', required=True)
    n1 = _field.Field(types.Real, 'Polyhedron four-digit side specificer #1', required=True)
    n2 = _field.Field(types.Real, 'Polyhedron four-digit side specificer #2', required=True)
    n3 = _field.Field(types.Real, 'Polyhedron four-digit side specificer #3', required=True)
    n4 = _field.Field(types.Real, 'Polyhedron four-digit side specificer #4', required=True)
    n5 = _field.Field(types.Real, 'Polyhedron four-digit side specificer #5', required=True)
    n6 = _field.Field(types.Real, 'Polyhedron four-digit side specificer #6', required=True)

    _REGEX = re.compile(
        rf'\A(\+|\*)?(\S+)( \S+)? arb( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z',
        re.IGNORECASE,
    )
