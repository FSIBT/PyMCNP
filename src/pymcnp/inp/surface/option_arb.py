import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser
from ...utils import _visualization


class SurfaceOption_Arb(_option.SurfaceOption_, keyword='arb'):
    """
    Represents INP surface card arb options.

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

    _REGEX = re.compile(
        r'\Aarb( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)\Z'
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
        Initializes ``SurfaceOption_Arb``.

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

        Returns:
            ``SurfaceOption_Arb``.

        Raises:
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
        """

        if ax is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, ax)
        if ay is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, ay)
        if az is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, az)
        if bx is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, bx)
        if by is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, by)
        if bz is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, bz)
        if cx is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, cx)
        if cy is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, cy)
        if cz is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, cz)
        if dx is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, dx)
        if dy is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, dy)
        if dz is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, dz)
        if ex is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, ex)
        if ey is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, ey)
        if ez is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, ez)
        if fx is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, fx)
        if fy is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, fy)
        if fz is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, fz)
        if gx is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, gx)
        if gy is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, gy)
        if gz is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, gz)
        if hx is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, hx)
        if hy is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, hy)
        if hz is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, hz)
        if n1 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, n1)
        if n2 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, n2)
        if n3 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, n3)
        if n4 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, n4)
        if n5 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, n5)
        if n6 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, n6)

        self.value: typing.Final[tuple[any]] = types._Tuple(
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

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SurfaceOption_Arb`` from INP.

        Parameters:
            source: INP surface card option.

        Returns:
            ``SurfaceOption_Arb``.

        Raises:
            McnpError: SYNTAX_SURFACE_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SurfaceOption_Arb._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_SURFACE_OPTION, source)

        ax = types.Real.from_mcnp(tokens[1])
        ay = types.Real.from_mcnp(tokens[2])
        az = types.Real.from_mcnp(tokens[3])
        bx = types.Real.from_mcnp(tokens[4])
        by = types.Real.from_mcnp(tokens[5])
        bz = types.Real.from_mcnp(tokens[6])
        cx = types.Real.from_mcnp(tokens[7])
        cy = types.Real.from_mcnp(tokens[8])
        cz = types.Real.from_mcnp(tokens[9])
        dx = types.Real.from_mcnp(tokens[10])
        dy = types.Real.from_mcnp(tokens[11])
        dz = types.Real.from_mcnp(tokens[12])
        ex = types.Real.from_mcnp(tokens[13])
        ey = types.Real.from_mcnp(tokens[14])
        ez = types.Real.from_mcnp(tokens[15])
        fx = types.Real.from_mcnp(tokens[16])
        fy = types.Real.from_mcnp(tokens[17])
        fz = types.Real.from_mcnp(tokens[18])
        gx = types.Real.from_mcnp(tokens[19])
        gy = types.Real.from_mcnp(tokens[20])
        gz = types.Real.from_mcnp(tokens[21])
        hx = types.Real.from_mcnp(tokens[22])
        hy = types.Real.from_mcnp(tokens[23])
        hz = types.Real.from_mcnp(tokens[24])
        n1 = types.Real.from_mcnp(tokens[25])
        n2 = types.Real.from_mcnp(tokens[26])
        n3 = types.Real.from_mcnp(tokens[27])
        n4 = types.Real.from_mcnp(tokens[28])
        n5 = types.Real.from_mcnp(tokens[29])
        n6 = types.Real.from_mcnp(tokens[30])

        return SurfaceOption_Arb(
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
        )

    def to_pyvista(self):
        """
        Generates ``pyvista.PolyData`` from ``SurfaceOption_Arb``.

        Returns:
            ``pyvista.PolyData`` for ``SurfaceOption_Arb``.
        """

        a = _visualization.Vector(self.ax.value, self.ay.value, self.az.value)
        b = _visualization.Vector(self.bx.value, self.by.value, self.bz.value)
        c = _visualization.Vector(self.cx.value, self.cy.value, self.cz.value)
        d = _visualization.Vector(self.dx.value, self.dy.value, self.dz.value)
        e = _visualization.Vector(self.ex.value, self.ey.value, self.ez.value)
        f = _visualization.Vector(self.fx.value, self.fy.value, self.fz.value)
        g = _visualization.Vector(self.gx.value, self.gy.value, self.gz.value)
        h = _visualization.Vector(self.hx.value, self.hy.value, self.hz.value)

        vectices = []
        for vec in [a, b, c, d, e, f, g, h]:
            if vec.x == 0 and vec.y == 0 and vec.z == 0:
                continue
            else:
                vectices.append(vec)

        faces = []
        for n in [
            self.n1.value,
            self.n2.value,
            self.n3.value,
            self.n4.value,
            self.n5.value,
            self.n6.value,
        ]:
            if n == 0:
                continue
            else:
                faces.append([n // 1000 % 10, n // 100 % 10, n // 10 % 10, n // 1 % 10])

        vis = _visualization.PyMcnpVisualization.get_polyhedron(vectices, faces)

        return vis.data
