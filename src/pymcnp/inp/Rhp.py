import re
import math

import numpy

from . import _field
from . import _card
from .. import _show
from .. import types
from .. import errors


class Rhp(_field.Fields, _card.Card):
    """
    Represents INP `rhp` surface cards.
    """

    _KEYWORD = 'rhp'

    _CODE = errors.InpCode.SEMANTICS_OPTION
    _ORDER = ('vx', 'vy', 'vz', 'hx', 'hy', 'hz', 'r1', 'r2', 'r3', 's1', 's2', 's3', 't1', 't2', 't3', 'number', 'transform', 'prefix')
    _SET = ('vx', 'vy', 'vz', 'hx', 'hy', 'hz', 'r1', 'r2', 'r3', 's1', 's2', 's3', 't1', 't2', 't3', 'transform', 'number', 'prefix')

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
    vx = _field.Field(types.Real, 'Hexagonal prism position vector x component', required=True)
    vy = _field.Field(types.Real, 'Hexagonal prism position vector y component', required=True)
    vz = _field.Field(types.Real, 'Hexagonal prism position vector z component', required=True)
    hx = _field.Field(types.Real, 'Hexagonal prism height vector x component', required=True)
    hy = _field.Field(types.Real, 'Hexagonal prism height vector y component', required=True)
    hz = _field.Field(types.Real, 'Hexagonal prism height vector z component', required=True)
    r1 = _field.Field(types.Real, 'Hexagonal prism facet #1 vector x component', required=True)
    r2 = _field.Field(types.Real, 'Hexagonal prism facet #1 vector y component', required=True)
    r3 = _field.Field(types.Real, 'Hexagonal prism facet #1 vector z component', required=True)
    s1 = _field.Field(types.Real, 'Hexagonal prism facet #2 vector x component')
    s2 = _field.Field(types.Real, 'Hexagonal prism facet #2 vector y component')
    s3 = _field.Field(types.Real, 'Hexagonal prism facet #2 vector z component')
    t1 = _field.Field(types.Real, 'Hexagonal prism facet #3 vector x component')
    t2 = _field.Field(types.Real, 'Hexagonal prism facet #3 vector y component')
    t3 = _field.Field(types.Real, 'Hexagonal prism facet #3 vector z component')

    _REGEX = re.compile(
        rf'\A(\+|\*)?(\S+)( \S+)? rhp( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?\Z',
        re.IGNORECASE,
    )

    def to_show(self, shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `Rhp`.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            `_show.Shape` for `Rhp`
        """

        v = numpy.array((float(self.vx), float(self.vy), float(self.vz)))
        h = numpy.array((float(self.hx), float(self.hy), float(self.hz)))
        r = numpy.array((float(self.r1), float(self.r2), float(self.r3)))
        s = numpy.array((float(self.s1), float(self.s2), float(self.s3)))
        t = numpy.array((float(self.t1), float(self.t2), float(self.t3)))

        cross = numpy.cross(v, numpy.array((0, 0, 1)))
        angle = numpy.degrees(numpy.arccos(v[2] / numpy.linalg.norm(v)))
        apothem_r = numpy.linalg.norm(r) * 2 / math.sqrt(3)
        apothem_s = numpy.linalg.norm(s) * 2 / math.sqrt(3)
        apothem_t = numpy.linalg.norm(t) * 2 / math.sqrt(3)

        vis = shapes.CylinderHexagonal(numpy.linalg.norm(h), apothem_r, apothem_s, apothem_t)
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
        Generates INP from `Rhp`.

        Returns:
            INP surface card.
        """

        source = f'{self.prefix if self.prefix is not None else ""}{self.number} {self.transform if self.transform is not None else ""} {self._KEYWORD} {self.vx} {self.vy} {self.vz} {self.hx} {self.hy} {self.hz} {self.r1} {self.r2} {self.r3} {self.s1 if self.s1 is not None else ""} {self.s2 if self.s2 is not None else ""} {self.s3 if self.s3 is not None else ""} {self.t1 if self.t1 is not None else ""} {self.t2 if self.t2 is not None else ""} {self.t3 if self.t3 is not None else ""}'
        source = _card.Card._postprocess(source)

        return source
