import re

import numpy

from . import _field
from . import _card
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


class P_1(_field.Fields, _card.Card):
    """
    Represents INP `p` surface cards variation #1.
    """

    _KEYWORD = 'p'

    _CODE = errors.InpCode.SEMANTICS_OPTION
    _ORDER = ('x1', 'y1', 'z1', 'x2', 'y2', 'z2', 'x3', 'y3', 'z3', 'number', 'transform', 'prefix')
    _SET = ('x1', 'y1', 'z1', 'x2', 'y2', 'z2', 'x3', 'y3', 'z3', 'transform', 'number', 'prefix')

    prefix = _field.Field(
        types.String, 'Surface whitebody/reflecting flag', numeric=(), invalid=lambda self, value: value is not None and value.value.lower() not in {'*', '+'}, code=errors.InpCode.SEMANTICS_CARD
    )
    number = _field.Field(
        types.Integer,
        'Surface number',
        required=True,
        default=lambda card: next(_card.NUMBER),
        numeric=int,
        invalid=lambda self, value: not 1 <= value <= (99999999 if not self.transform else 999),
        code=errors.InpCode.SEMANTICS_CARD,
    )
    transform = _field.Field(types.Integer, 'Surface transform', numeric=int, invalid=lambda self, value: value is not None and (not 0 <= value <= 999), code=errors.InpCode.SEMANTICS_CARD)
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

    def __and__(a, b):
        """
        Unites `Surface`.

        Parameters:
            a: Operand #1.
            b: Operand #2.

        Returns:
            `Surface` union.
        """

        return types.Geometry.from_mcnp(f'{a.number}:{b.number}')

    def __or__(a, b):
        """
        Intersects `Surface`.

        Parameters:
            a: Operand #1.
            b: Operand #2.

        Returns:
            `Surface` intersection.
        """

        return types.Geometry.from_mcnp(f'{a.number} {b.number}')

    def __neg__(self):
        """
        Negatives `Surface`.

        Returns:
            `Surface` negative.
        """

        return types.Geometry.from_mcnp(f'-{self.number}')

    def __pos__(self):
        """
        Positives `Surface`.

        Returns:
            `Surface` positive.
        """

        return types.Geometry.from_mcnp(f'+{self.number}')

    def __invert__(self):
        """
        Inverts `Surface`.

        Returns:
            `Surface` complement.
        """

        return types.Geometry.from_mcnp(f'#{self.number}')

    def to_mcnp(self):
        """
        Generates INP from `P_1`.

        Returns:
            INP surface card.
        """

        source = f'{self.prefix if self.prefix is not None else ""}{self.number} {self.transform if self.transform is not None else ""} {self._KEYWORD} {self.x1} {self.y1} {self.z1} {self.x2} {self.y2} {self.z2} {self.x3} {self.y3} {self.z3}'
        source = _card.Card._postprocess(source)

        return source
