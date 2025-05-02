import re
import typing
import dataclasses


from ._option import SurfaceOption
from ...utils import types
from ...utils import errors


class Arb(SurfaceOption):
    """
    Represents INP arb elements.

    Attributes:
        ax: Polyhedron corner #1 x component.
        ay: Polyhedron corner #1 y component.
        az: Polyhedron corner #1 z component.
        bx: Polyhedron corner #2 x component.
        by: Polyhedron corner #2 y component.
        bz: Polyhedron corner #2 z component.
        cx: Polyhedron corner #3 x component.
        cy: Polyhedron corner #3 y component.
        cz: Polyhedron corner #3 z component.
        dx: Polyhedron corner #4 x component.
        dy: Polyhedron corner #4 y component.
        dz: Polyhedron corner #4 z component.
        ex: Polyhedron corner #5 x component.
        ey: Polyhedron corner #5 y component.
        ez: Polyhedron corner #5 z component.
        fx: Polyhedron corner #6 x component.
        fy: Polyhedron corner #6 y component.
        fz: Polyhedron corner #6 z component.
        gx: Polyhedron corner #7 x component.
        gy: Polyhedron corner #7 y component.
        gz: Polyhedron corner #7 z component.
        hx: Polyhedron corner #8 x component.
        hy: Polyhedron corner #8 y component.
        hz: Polyhedron corner #8 z component.
        n1: Polyhedron four-digit side specificer #1.
        n2: Polyhedron four-digit side specificer #2.
        n3: Polyhedron four-digit side specificer #3.
        n4: Polyhedron four-digit side specificer #4.
        n5: Polyhedron four-digit side specificer #5.
        n6: Polyhedron four-digit side specificer #6.
    """

    _ATTRS = {
        'ax': types.Real,
        'ay': types.Real,
        'az': types.Real,
        'bx': types.Real,
        'by': types.Real,
        'bz': types.Real,
        'cx': types.Real,
        'cy': types.Real,
        'cz': types.Real,
        'dx': types.Real,
        'dy': types.Real,
        'dz': types.Real,
        'ex': types.Real,
        'ey': types.Real,
        'ez': types.Real,
        'fx': types.Real,
        'fy': types.Real,
        'fz': types.Real,
        'gx': types.Real,
        'gy': types.Real,
        'gz': types.Real,
        'hx': types.Real,
        'hy': types.Real,
        'hz': types.Real,
        'n1': types.Real,
        'n2': types.Real,
        'n3': types.Real,
        'n4': types.Real,
        'n5': types.Real,
        'n6': types.Real,
    }

    _REGEX = re.compile(
        rf'\Aarb( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})\Z'
    )

    def __init__(
        self,
        ax: types.Real,
        ay: types.Real,
        az: types.Real,
        bx: types.Real,
        by: types.Real,
        bz: types.Real,
        cx: types.Real,
        cy: types.Real,
        cz: types.Real,
        dx: types.Real,
        dy: types.Real,
        dz: types.Real,
        ex: types.Real,
        ey: types.Real,
        ez: types.Real,
        fx: types.Real,
        fy: types.Real,
        fz: types.Real,
        gx: types.Real,
        gy: types.Real,
        gz: types.Real,
        hx: types.Real,
        hy: types.Real,
        hz: types.Real,
        n1: types.Real,
        n2: types.Real,
        n3: types.Real,
        n4: types.Real,
        n5: types.Real,
        n6: types.Real,
    ):
        """
        Initializes ``Arb``.

        Parameters:
            ax: Polyhedron corner #1 x component.
            ay: Polyhedron corner #1 y component.
            az: Polyhedron corner #1 z component.
            bx: Polyhedron corner #2 x component.
            by: Polyhedron corner #2 y component.
            bz: Polyhedron corner #2 z component.
            cx: Polyhedron corner #3 x component.
            cy: Polyhedron corner #3 y component.
            cz: Polyhedron corner #3 z component.
            dx: Polyhedron corner #4 x component.
            dy: Polyhedron corner #4 y component.
            dz: Polyhedron corner #4 z component.
            ex: Polyhedron corner #5 x component.
            ey: Polyhedron corner #5 y component.
            ez: Polyhedron corner #5 z component.
            fx: Polyhedron corner #6 x component.
            fy: Polyhedron corner #6 y component.
            fz: Polyhedron corner #6 z component.
            gx: Polyhedron corner #7 x component.
            gy: Polyhedron corner #7 y component.
            gz: Polyhedron corner #7 z component.
            hx: Polyhedron corner #8 x component.
            hy: Polyhedron corner #8 y component.
            hz: Polyhedron corner #8 z component.
            n1: Polyhedron four-digit side specificer #1.
            n2: Polyhedron four-digit side specificer #2.
            n3: Polyhedron four-digit side specificer #3.
            n4: Polyhedron four-digit side specificer #4.
            n5: Polyhedron four-digit side specificer #5.
            n6: Polyhedron four-digit side specificer #6.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if ax is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ax)
        if ay is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ay)
        if az is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, az)
        if bx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bx)
        if by is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, by)
        if bz is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bz)
        if cx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, cx)
        if cy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, cy)
        if cz is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, cz)
        if dx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, dx)
        if dy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, dy)
        if dz is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, dz)
        if ex is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ex)
        if ey is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ey)
        if ez is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ez)
        if fx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, fx)
        if fy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, fy)
        if fz is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, fz)
        if gx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, gx)
        if gy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, gy)
        if gz is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, gz)
        if hx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, hx)
        if hy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, hy)
        if hz is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, hz)
        if n1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, n1)
        if n2 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, n2)
        if n3 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, n3)
        if n4 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, n4)
        if n5 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, n5)
        if n6 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, n6)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                ax,
                ay,
                az,
                bx,
                by,
                bz,
                cx,
                cy,
                cz,
                dx,
                dy,
                dz,
                ex,
                ey,
                ez,
                fx,
                fy,
                fz,
                gx,
                gy,
                gz,
                hx,
                hy,
                hz,
                n1,
                n2,
                n3,
                n4,
                n5,
                n6,
            ]
        )

        self.ax: typing.Final[types.Real] = ax
        self.ay: typing.Final[types.Real] = ay
        self.az: typing.Final[types.Real] = az
        self.bx: typing.Final[types.Real] = bx
        self.by: typing.Final[types.Real] = by
        self.bz: typing.Final[types.Real] = bz
        self.cx: typing.Final[types.Real] = cx
        self.cy: typing.Final[types.Real] = cy
        self.cz: typing.Final[types.Real] = cz
        self.dx: typing.Final[types.Real] = dx
        self.dy: typing.Final[types.Real] = dy
        self.dz: typing.Final[types.Real] = dz
        self.ex: typing.Final[types.Real] = ex
        self.ey: typing.Final[types.Real] = ey
        self.ez: typing.Final[types.Real] = ez
        self.fx: typing.Final[types.Real] = fx
        self.fy: typing.Final[types.Real] = fy
        self.fz: typing.Final[types.Real] = fz
        self.gx: typing.Final[types.Real] = gx
        self.gy: typing.Final[types.Real] = gy
        self.gz: typing.Final[types.Real] = gz
        self.hx: typing.Final[types.Real] = hx
        self.hy: typing.Final[types.Real] = hy
        self.hz: typing.Final[types.Real] = hz
        self.n1: typing.Final[types.Real] = n1
        self.n2: typing.Final[types.Real] = n2
        self.n3: typing.Final[types.Real] = n3
        self.n4: typing.Final[types.Real] = n4
        self.n5: typing.Final[types.Real] = n5
        self.n6: typing.Final[types.Real] = n6


@dataclasses.dataclass
class ArbBuilder:
    """
    Builds ``Arb``.

    Attributes:
        ax: Polyhedron corner #1 x component.
        ay: Polyhedron corner #1 y component.
        az: Polyhedron corner #1 z component.
        bx: Polyhedron corner #2 x component.
        by: Polyhedron corner #2 y component.
        bz: Polyhedron corner #2 z component.
        cx: Polyhedron corner #3 x component.
        cy: Polyhedron corner #3 y component.
        cz: Polyhedron corner #3 z component.
        dx: Polyhedron corner #4 x component.
        dy: Polyhedron corner #4 y component.
        dz: Polyhedron corner #4 z component.
        ex: Polyhedron corner #5 x component.
        ey: Polyhedron corner #5 y component.
        ez: Polyhedron corner #5 z component.
        fx: Polyhedron corner #6 x component.
        fy: Polyhedron corner #6 y component.
        fz: Polyhedron corner #6 z component.
        gx: Polyhedron corner #7 x component.
        gy: Polyhedron corner #7 y component.
        gz: Polyhedron corner #7 z component.
        hx: Polyhedron corner #8 x component.
        hy: Polyhedron corner #8 y component.
        hz: Polyhedron corner #8 z component.
        n1: Polyhedron four-digit side specificer #1.
        n2: Polyhedron four-digit side specificer #2.
        n3: Polyhedron four-digit side specificer #3.
        n4: Polyhedron four-digit side specificer #4.
        n5: Polyhedron four-digit side specificer #5.
        n6: Polyhedron four-digit side specificer #6.
    """

    ax: str | float | types.Real
    ay: str | float | types.Real
    az: str | float | types.Real
    bx: str | float | types.Real
    by: str | float | types.Real
    bz: str | float | types.Real
    cx: str | float | types.Real
    cy: str | float | types.Real
    cz: str | float | types.Real
    dx: str | float | types.Real
    dy: str | float | types.Real
    dz: str | float | types.Real
    ex: str | float | types.Real
    ey: str | float | types.Real
    ez: str | float | types.Real
    fx: str | float | types.Real
    fy: str | float | types.Real
    fz: str | float | types.Real
    gx: str | float | types.Real
    gy: str | float | types.Real
    gz: str | float | types.Real
    hx: str | float | types.Real
    hy: str | float | types.Real
    hz: str | float | types.Real
    n1: str | float | types.Real
    n2: str | float | types.Real
    n3: str | float | types.Real
    n4: str | float | types.Real
    n5: str | float | types.Real
    n6: str | float | types.Real

    def build(self):
        """
        Builds ``ArbBuilder`` into ``Arb``.

        Returns:
            ``Arb`` for ``ArbBuilder``.
        """

        if isinstance(self.ax, types.Real):
            ax = self.ax
        elif isinstance(self.ax, float) or isinstance(self.ax, int):
            ax = types.Real(self.ax)
        elif isinstance(self.ax, str):
            ax = types.Real.from_mcnp(self.ax)

        if isinstance(self.ay, types.Real):
            ay = self.ay
        elif isinstance(self.ay, float) or isinstance(self.ay, int):
            ay = types.Real(self.ay)
        elif isinstance(self.ay, str):
            ay = types.Real.from_mcnp(self.ay)

        if isinstance(self.az, types.Real):
            az = self.az
        elif isinstance(self.az, float) or isinstance(self.az, int):
            az = types.Real(self.az)
        elif isinstance(self.az, str):
            az = types.Real.from_mcnp(self.az)

        if isinstance(self.bx, types.Real):
            bx = self.bx
        elif isinstance(self.bx, float) or isinstance(self.bx, int):
            bx = types.Real(self.bx)
        elif isinstance(self.bx, str):
            bx = types.Real.from_mcnp(self.bx)

        if isinstance(self.by, types.Real):
            by = self.by
        elif isinstance(self.by, float) or isinstance(self.by, int):
            by = types.Real(self.by)
        elif isinstance(self.by, str):
            by = types.Real.from_mcnp(self.by)

        if isinstance(self.bz, types.Real):
            bz = self.bz
        elif isinstance(self.bz, float) or isinstance(self.bz, int):
            bz = types.Real(self.bz)
        elif isinstance(self.bz, str):
            bz = types.Real.from_mcnp(self.bz)

        if isinstance(self.cx, types.Real):
            cx = self.cx
        elif isinstance(self.cx, float) or isinstance(self.cx, int):
            cx = types.Real(self.cx)
        elif isinstance(self.cx, str):
            cx = types.Real.from_mcnp(self.cx)

        if isinstance(self.cy, types.Real):
            cy = self.cy
        elif isinstance(self.cy, float) or isinstance(self.cy, int):
            cy = types.Real(self.cy)
        elif isinstance(self.cy, str):
            cy = types.Real.from_mcnp(self.cy)

        if isinstance(self.cz, types.Real):
            cz = self.cz
        elif isinstance(self.cz, float) or isinstance(self.cz, int):
            cz = types.Real(self.cz)
        elif isinstance(self.cz, str):
            cz = types.Real.from_mcnp(self.cz)

        if isinstance(self.dx, types.Real):
            dx = self.dx
        elif isinstance(self.dx, float) or isinstance(self.dx, int):
            dx = types.Real(self.dx)
        elif isinstance(self.dx, str):
            dx = types.Real.from_mcnp(self.dx)

        if isinstance(self.dy, types.Real):
            dy = self.dy
        elif isinstance(self.dy, float) or isinstance(self.dy, int):
            dy = types.Real(self.dy)
        elif isinstance(self.dy, str):
            dy = types.Real.from_mcnp(self.dy)

        if isinstance(self.dz, types.Real):
            dz = self.dz
        elif isinstance(self.dz, float) or isinstance(self.dz, int):
            dz = types.Real(self.dz)
        elif isinstance(self.dz, str):
            dz = types.Real.from_mcnp(self.dz)

        if isinstance(self.ex, types.Real):
            ex = self.ex
        elif isinstance(self.ex, float) or isinstance(self.ex, int):
            ex = types.Real(self.ex)
        elif isinstance(self.ex, str):
            ex = types.Real.from_mcnp(self.ex)

        if isinstance(self.ey, types.Real):
            ey = self.ey
        elif isinstance(self.ey, float) or isinstance(self.ey, int):
            ey = types.Real(self.ey)
        elif isinstance(self.ey, str):
            ey = types.Real.from_mcnp(self.ey)

        if isinstance(self.ez, types.Real):
            ez = self.ez
        elif isinstance(self.ez, float) or isinstance(self.ez, int):
            ez = types.Real(self.ez)
        elif isinstance(self.ez, str):
            ez = types.Real.from_mcnp(self.ez)

        if isinstance(self.fx, types.Real):
            fx = self.fx
        elif isinstance(self.fx, float) or isinstance(self.fx, int):
            fx = types.Real(self.fx)
        elif isinstance(self.fx, str):
            fx = types.Real.from_mcnp(self.fx)

        if isinstance(self.fy, types.Real):
            fy = self.fy
        elif isinstance(self.fy, float) or isinstance(self.fy, int):
            fy = types.Real(self.fy)
        elif isinstance(self.fy, str):
            fy = types.Real.from_mcnp(self.fy)

        if isinstance(self.fz, types.Real):
            fz = self.fz
        elif isinstance(self.fz, float) or isinstance(self.fz, int):
            fz = types.Real(self.fz)
        elif isinstance(self.fz, str):
            fz = types.Real.from_mcnp(self.fz)

        if isinstance(self.gx, types.Real):
            gx = self.gx
        elif isinstance(self.gx, float) or isinstance(self.gx, int):
            gx = types.Real(self.gx)
        elif isinstance(self.gx, str):
            gx = types.Real.from_mcnp(self.gx)

        if isinstance(self.gy, types.Real):
            gy = self.gy
        elif isinstance(self.gy, float) or isinstance(self.gy, int):
            gy = types.Real(self.gy)
        elif isinstance(self.gy, str):
            gy = types.Real.from_mcnp(self.gy)

        if isinstance(self.gz, types.Real):
            gz = self.gz
        elif isinstance(self.gz, float) or isinstance(self.gz, int):
            gz = types.Real(self.gz)
        elif isinstance(self.gz, str):
            gz = types.Real.from_mcnp(self.gz)

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

        if isinstance(self.n1, types.Real):
            n1 = self.n1
        elif isinstance(self.n1, float) or isinstance(self.n1, int):
            n1 = types.Real(self.n1)
        elif isinstance(self.n1, str):
            n1 = types.Real.from_mcnp(self.n1)

        if isinstance(self.n2, types.Real):
            n2 = self.n2
        elif isinstance(self.n2, float) or isinstance(self.n2, int):
            n2 = types.Real(self.n2)
        elif isinstance(self.n2, str):
            n2 = types.Real.from_mcnp(self.n2)

        if isinstance(self.n3, types.Real):
            n3 = self.n3
        elif isinstance(self.n3, float) or isinstance(self.n3, int):
            n3 = types.Real(self.n3)
        elif isinstance(self.n3, str):
            n3 = types.Real.from_mcnp(self.n3)

        if isinstance(self.n4, types.Real):
            n4 = self.n4
        elif isinstance(self.n4, float) or isinstance(self.n4, int):
            n4 = types.Real(self.n4)
        elif isinstance(self.n4, str):
            n4 = types.Real.from_mcnp(self.n4)

        if isinstance(self.n5, types.Real):
            n5 = self.n5
        elif isinstance(self.n5, float) or isinstance(self.n5, int):
            n5 = types.Real(self.n5)
        elif isinstance(self.n5, str):
            n5 = types.Real.from_mcnp(self.n5)

        if isinstance(self.n6, types.Real):
            n6 = self.n6
        elif isinstance(self.n6, float) or isinstance(self.n6, int):
            n6 = types.Real(self.n6)
        elif isinstance(self.n6, str):
            n6 = types.Real.from_mcnp(self.n6)

        return Arb(
            ax=ax,
            ay=ay,
            az=az,
            bx=bx,
            by=by,
            bz=bz,
            cx=cx,
            cy=cy,
            cz=cz,
            dx=dx,
            dy=dy,
            dz=dz,
            ex=ex,
            ey=ey,
            ez=ez,
            fx=fx,
            fy=fy,
            fz=fz,
            gx=gx,
            gy=gy,
            gz=gz,
            hx=hx,
            hy=hy,
            hz=hz,
            n1=n1,
            n2=n2,
            n3=n3,
            n4=n4,
            n5=n5,
            n6=n6,
        )
