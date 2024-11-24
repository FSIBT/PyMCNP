"""
Contains the ``Arb`` subclass of ``Surface``."""

from typing import Final

from ..surface import Surface, SurfaceMnemonic
from ....utils import types, errors, _parser


class Arb(Surface):
    """
    Represents INP arb surface cards.

    ``Arb`` implements ``Surface``.

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

    def __init__(
        self,
        number: types.McnpInteger,
        transform: types.McnpInteger,
        ax: types.McnpReal,
        ay: types.McnpReal,
        az: types.McnpReal,
        bx: types.McnpReal,
        by: types.McnpReal,
        bz: types.McnpReal,
        cx: types.McnpReal,
        cy: types.McnpReal,
        cz: types.McnpReal,
        dx: types.McnpReal,
        dy: types.McnpReal,
        dz: types.McnpReal,
        ex: types.McnpReal,
        ey: types.McnpReal,
        ez: types.McnpReal,
        fx: types.McnpReal,
        fy: types.McnpReal,
        fz: types.McnpReal,
        gx: types.McnpReal,
        gy: types.McnpReal,
        gz: types.McnpReal,
        hx: types.McnpReal,
        hy: types.McnpReal,
        hz: types.McnpReal,
        n1: types.McnpReal,
        n2: types.McnpReal,
        n3: types.McnpReal,
        n4: types.McnpReal,
        n5: types.McnpReal,
        n6: types.McnpReal,
        is_whiteboundary: bool = False,
        is_reflecting: bool = False,
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
            McnpError: INVALID_SURFACE_NUMBER.
            McnpError: INVALID_SURFACE_TRANSFORMPERIODIC.
            McnpError: INVALID_SURFACE_WHITEBOUNDARY.
            McnpError: INVALID_SURFACE_REFLECTING.
            McnpError: INVALID_SURFACE_PARAMETER.
        """

        if number is None or not (1 <= number <= 99_999_999):
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_NUMBER, str(number))

        if transform is not None and not (-99_999_999 <= transform <= 999):
            raise errors.McnpError(
                errors.McnpCode.INVALID_SURFACE_TRANSFORMPERIODIC, str(transform)
            )

        if is_whiteboundary is None:
            raise errors.McnpError(
                errors.McnpCode.INVALID_SURFACE_WHITEBOUNDARY, str(is_whiteboundary)
            )

        if is_reflecting is None or (is_reflecting and is_whiteboundary):
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_REFLECTING, str(is_reflecting))

        if ax is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(ax))

        if ay is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(ay))

        if az is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(az))

        if bx is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(bx))

        if by is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(by))

        if bz is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(bz))

        if cx is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(cx))

        if cy is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(cy))

        if cz is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(cz))

        if dx is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(dx))

        if dy is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(dy))

        if dz is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(dz))

        if ex is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(ex))

        if ey is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(ey))

        if ez is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(ez))

        if fx is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(fx))

        if fy is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(fy))

        if fz is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(fz))

        if gx is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(gx))

        if gy is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(gy))

        if gz is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(gz))

        if hx is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(hx))

        if hy is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(hy))

        if hz is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(hz))

        if n1 is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(n1))

        if n2 is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(n2))

        if n3 is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(n3))

        if n4 is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(n4))

        if n5 is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(n5))

        if n6 is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(n6))

        self.ident: Final[int] = number.value
        self.number: Final[types.McnpInteger] = number
        self.mnemonic: Final[SurfaceMnemonic] = SurfaceMnemonic.ARB
        self.transform: Final[types.McnpInteger] = transform
        self.is_reflecting: Final[bool] = is_reflecting
        self.is_whiteboundary: Final[bool] = is_whiteboundary

        self.ax: Final[types.McnpReal] = ax
        self.ay: Final[types.McnpReal] = ay
        self.az: Final[types.McnpReal] = az
        self.bx: Final[types.McnpReal] = bx
        self.by: Final[types.McnpReal] = by
        self.bz: Final[types.McnpReal] = bz
        self.cx: Final[types.McnpReal] = cx
        self.cy: Final[types.McnpReal] = cy
        self.cz: Final[types.McnpReal] = cz
        self.dx: Final[types.McnpReal] = dx
        self.dy: Final[types.McnpReal] = dy
        self.dz: Final[types.McnpReal] = dz
        self.ex: Final[types.McnpReal] = ex
        self.ey: Final[types.McnpReal] = ey
        self.ez: Final[types.McnpReal] = ez
        self.fx: Final[types.McnpReal] = fx
        self.fy: Final[types.McnpReal] = fy
        self.fz: Final[types.McnpReal] = fz
        self.gx: Final[types.McnpReal] = gx
        self.gy: Final[types.McnpReal] = gy
        self.gz: Final[types.McnpReal] = gz
        self.hx: Final[types.McnpReal] = hx
        self.hy: Final[types.McnpReal] = hy
        self.hz: Final[types.McnpReal] = hz
        self.n1: Final[types.McnpReal] = n1
        self.n2: Final[types.McnpReal] = n2
        self.n3: Final[types.McnpReal] = n3
        self.n4: Final[types.McnpReal] = n4
        self.n5: Final[types.McnpReal] = n5
        self.n6: Final[types.McnpReal] = n6
        self.parameters: Final[tuple[types.McnpReal]] = tuple(
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

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Arb`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for surface.

        Returns:
            ``Arb`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        source, comments = _parser.Preprocessor.process_inp_comments(source)
        tokens = _parser.Parser(
            source.split(' '),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.peekl()[0] == '+':
            is_whiteboundary = True
            is_reflecting = False
            tokens.pushl(tokens.popl()[1:])
        elif tokens.peekl()[0] == '*':
            is_whiteboundary = False
            is_reflecting = True
            tokens.pushl(tokens.popl()[1:])
        else:
            is_whiteboundary = False
            is_reflecting = False

        number = types.McnpInteger.from_mcnp(tokens.popl())

        try:
            transform = types.McnpInteger.from_mcnp(tokens.peekl())
            tokens.popl()
        except Exception:
            transform = None

        mnemonic = SurfaceMnemonic.from_mcnp(tokens.popl())

        ax = types.McnpReal.from_mcnp(tokens.popl())
        ay = types.McnpReal.from_mcnp(tokens.popl())
        az = types.McnpReal.from_mcnp(tokens.popl())
        bx = types.McnpReal.from_mcnp(tokens.popl())
        by = types.McnpReal.from_mcnp(tokens.popl())
        bz = types.McnpReal.from_mcnp(tokens.popl())
        cx = types.McnpReal.from_mcnp(tokens.popl())
        cy = types.McnpReal.from_mcnp(tokens.popl())
        cz = types.McnpReal.from_mcnp(tokens.popl())
        dx = types.McnpReal.from_mcnp(tokens.popl())
        dy = types.McnpReal.from_mcnp(tokens.popl())
        dz = types.McnpReal.from_mcnp(tokens.popl())
        ex = types.McnpReal.from_mcnp(tokens.popl())
        ey = types.McnpReal.from_mcnp(tokens.popl())
        ez = types.McnpReal.from_mcnp(tokens.popl())
        fx = types.McnpReal.from_mcnp(tokens.popl())
        fy = types.McnpReal.from_mcnp(tokens.popl())
        fz = types.McnpReal.from_mcnp(tokens.popl())
        gx = types.McnpReal.from_mcnp(tokens.popl())
        gy = types.McnpReal.from_mcnp(tokens.popl())
        gz = types.McnpReal.from_mcnp(tokens.popl())
        hx = types.McnpReal.from_mcnp(tokens.popl())
        hy = types.McnpReal.from_mcnp(tokens.popl())
        hz = types.McnpReal.from_mcnp(tokens.popl())
        n1 = types.McnpReal.from_mcnp(tokens.popl())
        n2 = types.McnpReal.from_mcnp(tokens.popl())
        n3 = types.McnpReal.from_mcnp(tokens.popl())
        n4 = types.McnpReal.from_mcnp(tokens.popl())
        n5 = types.McnpReal.from_mcnp(tokens.popl())
        n6 = types.McnpReal.from_mcnp(tokens.popl())

        return Arb(
            number,
            transform,
            mnemonic,
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
            is_whiteboundary=is_whiteboundary,
            is_reflecting=is_reflecting,
        )
