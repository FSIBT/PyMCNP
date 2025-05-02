import re
import typing
import dataclasses


from ._option import SurfaceOption
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class Rhp(SurfaceOption):
    """
    Represents INP rhp elements.

    Attributes:
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
        rf'\Arhp( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})\Z'
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
            InpError: SEMANTICS_OPTION.
        """

        if vx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, vx)
        if vy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, vy)
        if vz is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, vz)
        if hx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, hx)
        if hy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, hy)
        if hz is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, hz)
        if r1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, r1)
        if r2 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, r2)
        if r3 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, r3)
        if s1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, s1)
        if s2 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, s2)
        if s3 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, s3)
        if t1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, t1)
        if t2 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, t2)
        if t3 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, t3)

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

    def draw(self):
        """
        Generates ``Visualization`` from ``Rhp``.

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

        vis = _visualization.Visualization.get_cylinder_hexagon(
            h.norm(), r.apothem(), s.apothem(), t.apothem()
        )
        vis = vis.add_rotation(cross, angle, (0, 0, 0))
        vis = vis.add_translation(v)

        return vis


@dataclasses.dataclass
class RhpBuilder:
    """
    Builds ``Rhp``.

    Attributes:
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
    """

    vx: str | float | types.Real
    vy: str | float | types.Real
    vz: str | float | types.Real
    hx: str | float | types.Real
    hy: str | float | types.Real
    hz: str | float | types.Real
    r1: str | float | types.Real
    r2: str | float | types.Real
    r3: str | float | types.Real
    s1: str | float | types.Real
    s2: str | float | types.Real
    s3: str | float | types.Real
    t1: str | float | types.Real
    t2: str | float | types.Real
    t3: str | float | types.Real

    def build(self):
        """
        Builds ``RhpBuilder`` into ``Rhp``.

        Returns:
            ``Rhp`` for ``RhpBuilder``.
        """

        if isinstance(self.vx, types.Real):
            vx = self.vx
        elif isinstance(self.vx, float) or isinstance(self.vx, int):
            vx = types.Real(self.vx)
        elif isinstance(self.vx, str):
            vx = types.Real.from_mcnp(self.vx)

        if isinstance(self.vy, types.Real):
            vy = self.vy
        elif isinstance(self.vy, float) or isinstance(self.vy, int):
            vy = types.Real(self.vy)
        elif isinstance(self.vy, str):
            vy = types.Real.from_mcnp(self.vy)

        if isinstance(self.vz, types.Real):
            vz = self.vz
        elif isinstance(self.vz, float) or isinstance(self.vz, int):
            vz = types.Real(self.vz)
        elif isinstance(self.vz, str):
            vz = types.Real.from_mcnp(self.vz)

        if isinstance(self.hx, types.Real):
            hx = self.hx
        elif isinstance(self.hx, float) or isinstance(self.hx, int):
            hx = types.Real(self.hx)
        elif isinstance(self.hx, str):
            hx = types.Real.from_mcnp(self.hx)

        if isinstance(self.hy, types.Real):
            hy = self.hy
        elif isinstance(self.hy, float) or isinstance(self.hy, int):
            hy = types.Real(self.hy)
        elif isinstance(self.hy, str):
            hy = types.Real.from_mcnp(self.hy)

        if isinstance(self.hz, types.Real):
            hz = self.hz
        elif isinstance(self.hz, float) or isinstance(self.hz, int):
            hz = types.Real(self.hz)
        elif isinstance(self.hz, str):
            hz = types.Real.from_mcnp(self.hz)

        if isinstance(self.r1, types.Real):
            r1 = self.r1
        elif isinstance(self.r1, float) or isinstance(self.r1, int):
            r1 = types.Real(self.r1)
        elif isinstance(self.r1, str):
            r1 = types.Real.from_mcnp(self.r1)

        if isinstance(self.r2, types.Real):
            r2 = self.r2
        elif isinstance(self.r2, float) or isinstance(self.r2, int):
            r2 = types.Real(self.r2)
        elif isinstance(self.r2, str):
            r2 = types.Real.from_mcnp(self.r2)

        if isinstance(self.r3, types.Real):
            r3 = self.r3
        elif isinstance(self.r3, float) or isinstance(self.r3, int):
            r3 = types.Real(self.r3)
        elif isinstance(self.r3, str):
            r3 = types.Real.from_mcnp(self.r3)

        if isinstance(self.s1, types.Real):
            s1 = self.s1
        elif isinstance(self.s1, float) or isinstance(self.s1, int):
            s1 = types.Real(self.s1)
        elif isinstance(self.s1, str):
            s1 = types.Real.from_mcnp(self.s1)

        if isinstance(self.s2, types.Real):
            s2 = self.s2
        elif isinstance(self.s2, float) or isinstance(self.s2, int):
            s2 = types.Real(self.s2)
        elif isinstance(self.s2, str):
            s2 = types.Real.from_mcnp(self.s2)

        if isinstance(self.s3, types.Real):
            s3 = self.s3
        elif isinstance(self.s3, float) or isinstance(self.s3, int):
            s3 = types.Real(self.s3)
        elif isinstance(self.s3, str):
            s3 = types.Real.from_mcnp(self.s3)

        if isinstance(self.t1, types.Real):
            t1 = self.t1
        elif isinstance(self.t1, float) or isinstance(self.t1, int):
            t1 = types.Real(self.t1)
        elif isinstance(self.t1, str):
            t1 = types.Real.from_mcnp(self.t1)

        if isinstance(self.t2, types.Real):
            t2 = self.t2
        elif isinstance(self.t2, float) or isinstance(self.t2, int):
            t2 = types.Real(self.t2)
        elif isinstance(self.t2, str):
            t2 = types.Real.from_mcnp(self.t2)

        if isinstance(self.t3, types.Real):
            t3 = self.t3
        elif isinstance(self.t3, float) or isinstance(self.t3, int):
            t3 = types.Real(self.t3)
        elif isinstance(self.t3, str):
            t3 = types.Real.from_mcnp(self.t3)

        return Rhp(
            vx=vx,
            vy=vy,
            vz=vz,
            hx=hx,
            hy=hy,
            hz=hz,
            r1=r1,
            r2=r2,
            r3=r3,
            s1=s1,
            s2=s2,
            s3=s3,
            t1=t1,
            t2=t2,
            t3=t3,
        )
