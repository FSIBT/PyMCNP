import re
import typing


from .option_ import SurfaceOption_
from ...utils import types
from ...utils import errors


class Arb(SurfaceOption_, keyword='arb'):
    """
    Represents INP arb elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
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
        rf'arb( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})'
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
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if ax is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ax)
        if ay is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ay)
        if az is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, az)
        if bx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bx)
        if by is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, by)
        if bz is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bz)
        if cx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, cx)
        if cy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, cy)
        if cz is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, cz)
        if dx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, dx)
        if dy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, dy)
        if dz is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, dz)
        if ex is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ex)
        if ey is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ey)
        if ez is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ez)
        if fx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, fx)
        if fy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, fy)
        if fz is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, fz)
        if gx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, gx)
        if gy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, gy)
        if gz is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, gz)
        if hx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, hx)
        if hy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, hy)
        if hz is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, hz)
        if n1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, n1)
        if n2 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, n2)
        if n3 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, n3)
        if n4 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, n4)
        if n5 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, n5)
        if n6 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, n6)

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
