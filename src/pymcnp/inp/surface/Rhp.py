import re
import typing


from .option_ import SurfaceOption_
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class Rhp(SurfaceOption_, keyword='rhp'):
    """
    Represents INP rhp elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'vx': types.Real,
        'vy': types.Real,
        'vz': types.Real,
        'hx': types.Real,
        'hy': types.Real,
        'hz': types.Real,
        'r1': types.Real,
        'r2': types.Real,
        'r3': types.Real,
        's1': types.Real,
        's2': types.Real,
        's3': types.Real,
        't1': types.Real,
        't2': types.Real,
        't3': types.Real,
    }

    _REGEX = re.compile(
        rf'rhp( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})'
    )

    def __init__(
        self,
        vx: types.Real,
        vy: types.Real,
        vz: types.Real,
        hx: types.Real,
        hy: types.Real,
        hz: types.Real,
        r1: types.Real,
        r2: types.Real,
        r3: types.Real,
        s1: types.Real,
        s2: types.Real,
        s3: types.Real,
        t1: types.Real,
        t2: types.Real,
        t3: types.Real,
    ):
        """
        Initializes ``Rhp``.

        Parameters:
            vx: Hexagonal prism position vector x component.
            vy: Hexagonal prism position vector y component.
            vz: Hexagonal prism position vector z component.
            hx: Hexagonal prism height vector x component.
            hy: Hexagonal prism height vector y component.
            hz: Hexagonal prism height vector z component.
            r1: Hexagonal prism facet #1 vector x component.
            r2: Hexagonal prism facet #1 vector y component.
            r3: Hexagonal prism facet #1 vector z component.
            s1: Hexagonal prism facet #2 vector x component.
            s2: Hexagonal prism facet #2 vector y component.
            s3: Hexagonal prism facet #2 vector z component.
            t1: Hexagonal prism facet #3 vector x component.
            t2: Hexagonal prism facet #3 vector y component.
            t3: Hexagonal prism facet #3 vector z component.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if vx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, vx)
        if vy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, vy)
        if vz is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, vz)
        if hx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, hx)
        if hy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, hy)
        if hz is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, hz)
        if r1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, r1)
        if r2 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, r2)
        if r3 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, r3)
        if s1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, s1)
        if s2 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, s2)
        if s3 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, s3)
        if t1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, t1)
        if t2 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, t2)
        if t3 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, t3)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                vx,
                vy,
                vz,
                hx,
                hy,
                hz,
                r1,
                r2,
                r3,
                s1,
                s2,
                s3,
                t1,
                t2,
                t3,
            ]
        )

        self.vx: typing.Final[types.Real] = vx
        self.vy: typing.Final[types.Real] = vy
        self.vz: typing.Final[types.Real] = vz
        self.hx: typing.Final[types.Real] = hx
        self.hy: typing.Final[types.Real] = hy
        self.hz: typing.Final[types.Real] = hz
        self.r1: typing.Final[types.Real] = r1
        self.r2: typing.Final[types.Real] = r2
        self.r3: typing.Final[types.Real] = r3
        self.s1: typing.Final[types.Real] = s1
        self.s2: typing.Final[types.Real] = s2
        self.s3: typing.Final[types.Real] = s3
        self.t1: typing.Final[types.Real] = t1
        self.t2: typing.Final[types.Real] = t2
        self.t3: typing.Final[types.Real] = t3

    def to_pyvista(self):
        """
        Generates ``pyvista.PolyData`` from ``Rhp``.

        Returns:
            ``pyvista.PolyData`` for ``Rhp``
        """

        v = _visualization.Vector(self.vx.value, self.vy.value, self.vz.value)
        h = _visualization.Vector(self.hx.value, self.hy.value, self.hz.value)
        r = _visualization.Vector(self.r1.value, self.r2.value, self.r3.value)
        s = _visualization.Vector(self.s1.value, self.s2.value, self.s3.value)
        t = _visualization.Vector(self.t1.value, self.t2.value, self.t3.value)

        cross = v * _visualization.Vector(0, 0, 1)
        angle = v & _visualization.Vector(0, 0, 1)

        vis = _visualization.McnpVisualization.get_cylinder_hexagon(
            h.norm(), r.apothem(), s.apothem(), t.apothem()
        )
        vis = vis.add_rotation(cross, angle, (0, 0, 0))
        vis = vis.add_translation(v)

        return vis
