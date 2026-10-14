import re

import numpy

from . import _field
from . import _surface
from .. import _show
from .. import types
from .. import errors


def _coordinate(name, doc):
    return _field.Field(types.Real, doc, required=True, invalid=lambda self, value: _collinear(self, name, value))


def _collinear(card, name, value):
    """
    Checks that the three points would be collinear.
    """

    points = {n: value if n == name else getattr(card, '_' + n, None) for n in ('x1', 'y1', 'z1', 'x2', 'y2', 'z2', 'x3', 'y3', 'z3')}
    if any(v is None for v in points.values()):
        return False

    a = numpy.array([float(points[f'{axis}2'] - points[f'{axis}1']) for axis in 'xyz'])
    b = numpy.array([float(points[f'{axis}3'] - points[f'{axis}1']) for axis in 'xyz'])

    return not numpy.cross(a, b).any()


class P_1(_surface.Surface):
    """
    Represents INP `p` surface cards variation #1.
    """

    _KEYWORD = 'p'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    x1 = _coordinate('x1', 'Point-defined general plane x-coordinate #1')
    y1 = _coordinate('y1', 'Point-defined general plane y-coordinate #1')
    z1 = _coordinate('z1', 'Point-defined general plane z-coordinate #1')
    x2 = _coordinate('x2', 'Point-defined general plane x-coordinate #2')
    y2 = _coordinate('y2', 'Point-defined general plane y-coordinate #2')
    z2 = _coordinate('z2', 'Point-defined general plane z-coordinate #2')
    x3 = _coordinate('x3', 'Point-defined general plane x-coordinate #3')
    y3 = _coordinate('y3', 'Point-defined general plane y-coordinate #3')
    z3 = _coordinate('z3', 'Point-defined general plane z-coordinate #3')

    _REGEX = re.compile(
        rf'\A(\+|\*)?(\S+)( \S+)? p( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z',
        re.IGNORECASE,
    )

    def to_show(self, shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `P_1`.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            `_show.Shape` for `P_1`
        """

        a = numpy.array((float(self._x2 - self._x1), float(self._y2 - self._y1), float(self._z2 - self._z1)))
        b = numpy.array((float(self._x3 - self._x1), float(self._y3 - self._y1), float(self._z3 - self._z1)))
        n = numpy.cross(a, b)

        vis = shapes.Plane(n[0], n[1], n[2], n[0] * float(self._x1) + n[1] * float(self._y1) + n[2] * float(self._z1))

        return vis
