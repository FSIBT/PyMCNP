import re

import numpy

from . import _field
from . import _card
from .. import _show
from .. import types
from .. import errors


class Rec(_field.Fields, _card.Card):
    """
    Represents INP `rec` surface cards.
    """

    _KEYWORD = 'rec'

    _CODE = errors.InpCode.SEMANTICS_OPTION
    _ORDER = ('vx', 'vy', 'vz', 'hx', 'hy', 'hz', 'v1x', 'v1y', 'v1z', 'v2x', 'v2y', 'v2z', 'number', 'transform', 'prefix')
    _SET = ('vx', 'vy', 'vz', 'hx', 'hy', 'hz', 'v1x', 'v1y', 'v1z', 'v2x', 'v2y', 'v2z', 'transform', 'number', 'prefix')

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
    vx = _field.Field(types.Real, 'Elliptical cylinder position vector x component', required=True)
    vy = _field.Field(types.Real, 'Elliptical cylinder position vector y component', required=True)
    vz = _field.Field(types.Real, 'Elliptical cylinder position vector z component', required=True)
    hx = _field.Field(types.Real, 'Elliptical cylinder height vector x component', required=True)
    hy = _field.Field(types.Real, 'Elliptical cylinder height vector y component', required=True)
    hz = _field.Field(types.Real, 'Elliptical cylinder height vector z component', required=True)
    v1x = _field.Field(types.Real, 'Elliptical cylinder major axis vector x component', required=True)
    v1y = _field.Field(types.Real, 'Elliptical cylinder major axis vector y component', required=True)
    v1z = _field.Field(types.Real, 'Elliptical cylinder major axis vector z component', required=True)
    v2x = _field.Field(types.Real, 'Elliptical cylinder minor axis vector x component', required=True)
    v2y = _field.Field(types.Real, 'Elliptical cylinder minor axis vector y component')
    v2z = _field.Field(types.Real, 'Elliptical cylinder minor axis vector z component')

    _REGEX = re.compile(
        rf'\A(\+|\*)?(\S+)( \S+)? rec( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?\Z',
        re.IGNORECASE,
    )

    def to_show(self, shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `Rec`.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            `_show.Shape` for `Rec`
        """

        v = numpy.array((float(self.vx), float(self.vy), float(self.vz)))
        h = numpy.array((float(self.hx), float(self.hy), float(self.hz)))
        v1 = numpy.array((float(self.v1x), float(self.v1y), float(self.v1z)))
        v2 = numpy.array((float(self.v2x), float(self.v2y), float(self.v2z)))

        cross = numpy.cross(v, numpy.array((0, 0, 1)))
        angle = numpy.degrees(numpy.arccos(v[2] / numpy.linalg.norm(v)))

        vis = shapes.CylinderElliptical(numpy.linalg.norm(h), numpy.linalg.norm(v1), numpy.linalg.norm(v2))
        vis = vis.rotate(cross, angle, (0, 0, 0))
        vis = vis.translate(v)

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
        Generates INP from `Rec`.

        Returns:
            INP surface card.
        """

        source = f'{self.prefix if self.prefix is not None else ""}{self.number} {self.transform if self.transform is not None else ""} {self._KEYWORD} {self.vx} {self.vy} {self.vz} {self.hx} {self.hy} {self.hz} {self.v1x} {self.v1y} {self.v1z} {self.v2x} {self.v2y if self.v2y is not None else ""} {self.v2z if self.v2z is not None else ""}'
        source = _card.Card._postprocess(source)

        return source
