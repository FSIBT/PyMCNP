import re

from . import _option
from ... import types
from ... import errors


class Arb(_option.SurfaceOption):
    """
    Represents INP `arb` elements.
    """

    _KEYWORD = 'arb'

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
        rf'\Aarb( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z',
        re.IGNORECASE,
    )

    def __init__(
        self,
        ax: str | int | float | types.Real,
        ay: str | int | float | types.Real,
        az: str | int | float | types.Real,
        bx: str | int | float | types.Real,
        by: str | int | float | types.Real,
        bz: str | int | float | types.Real,
        cx: str | int | float | types.Real,
        cy: str | int | float | types.Real,
        cz: str | int | float | types.Real,
        dx: str | int | float | types.Real,
        dy: str | int | float | types.Real,
        dz: str | int | float | types.Real,
        ex: str | int | float | types.Real,
        ey: str | int | float | types.Real,
        ez: str | int | float | types.Real,
        fx: str | int | float | types.Real,
        fy: str | int | float | types.Real,
        fz: str | int | float | types.Real,
        gx: str | int | float | types.Real,
        gy: str | int | float | types.Real,
        gz: str | int | float | types.Real,
        hx: str | int | float | types.Real,
        hy: str | int | float | types.Real,
        hz: str | int | float | types.Real,
        n1: str | int | float | types.Real,
        n2: str | int | float | types.Real,
        n3: str | int | float | types.Real,
        n4: str | int | float | types.Real,
        n5: str | int | float | types.Real,
        n6: str | int | float | types.Real,
    ):
        """
        Initializes `Arb`.

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

        self.ax: types.Real = ax
        self.ay: types.Real = ay
        self.az: types.Real = az
        self.bx: types.Real = bx
        self.by: types.Real = by
        self.bz: types.Real = bz
        self.cx: types.Real = cx
        self.cy: types.Real = cy
        self.cz: types.Real = cz
        self.dx: types.Real = dx
        self.dy: types.Real = dy
        self.dz: types.Real = dz
        self.ex: types.Real = ex
        self.ey: types.Real = ey
        self.ez: types.Real = ez
        self.fx: types.Real = fx
        self.fy: types.Real = fy
        self.fz: types.Real = fz
        self.gx: types.Real = gx
        self.gy: types.Real = gy
        self.gz: types.Real = gz
        self.hx: types.Real = hx
        self.hy: types.Real = hy
        self.hz: types.Real = hz
        self.n1: types.Real = n1
        self.n2: types.Real = n2
        self.n3: types.Real = n3
        self.n4: types.Real = n4
        self.n5: types.Real = n5
        self.n6: types.Real = n6

    @property
    def ax(self) -> types.Real:
        """
        Polyhedron corner #1 x component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._ax

    @ax.setter
    def ax(self, ax: str | int | float | types.Real) -> None:
        """
        Sets `ax`.

        Parameters:
            ax: Polyhedron corner #1 x component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if ax is not None:
            if isinstance(ax, types.Real):
                ax = ax
            elif isinstance(ax, int) or isinstance(ax, float):
                ax = types.Real(ax)
            elif isinstance(ax, str):
                ax = types.Real.from_mcnp(ax)

        if ax is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ax)

        self._ax: types.Real = ax

    @property
    def ay(self) -> types.Real:
        """
        Polyhedron corner #1 y component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._ay

    @ay.setter
    def ay(self, ay: str | int | float | types.Real) -> None:
        """
        Sets `ay`.

        Parameters:
            ay: Polyhedron corner #1 y component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if ay is not None:
            if isinstance(ay, types.Real):
                ay = ay
            elif isinstance(ay, int) or isinstance(ay, float):
                ay = types.Real(ay)
            elif isinstance(ay, str):
                ay = types.Real.from_mcnp(ay)

        if ay is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ay)

        self._ay: types.Real = ay

    @property
    def az(self) -> types.Real:
        """
        Polyhedron corner #1 z component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._az

    @az.setter
    def az(self, az: str | int | float | types.Real) -> None:
        """
        Sets `az`.

        Parameters:
            az: Polyhedron corner #1 z component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if az is not None:
            if isinstance(az, types.Real):
                az = az
            elif isinstance(az, int) or isinstance(az, float):
                az = types.Real(az)
            elif isinstance(az, str):
                az = types.Real.from_mcnp(az)

        if az is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, az)

        self._az: types.Real = az

    @property
    def bx(self) -> types.Real:
        """
        Polyhedron corner #2 x component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._bx

    @bx.setter
    def bx(self, bx: str | int | float | types.Real) -> None:
        """
        Sets `bx`.

        Parameters:
            bx: Polyhedron corner #2 x component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if bx is not None:
            if isinstance(bx, types.Real):
                bx = bx
            elif isinstance(bx, int) or isinstance(bx, float):
                bx = types.Real(bx)
            elif isinstance(bx, str):
                bx = types.Real.from_mcnp(bx)

        if bx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bx)

        self._bx: types.Real = bx

    @property
    def by(self) -> types.Real:
        """
        Polyhedron corner #2 y component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._by

    @by.setter
    def by(self, by: str | int | float | types.Real) -> None:
        """
        Sets `by`.

        Parameters:
            by: Polyhedron corner #2 y component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if by is not None:
            if isinstance(by, types.Real):
                by = by
            elif isinstance(by, int) or isinstance(by, float):
                by = types.Real(by)
            elif isinstance(by, str):
                by = types.Real.from_mcnp(by)

        if by is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, by)

        self._by: types.Real = by

    @property
    def bz(self) -> types.Real:
        """
        Polyhedron corner #2 z component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._bz

    @bz.setter
    def bz(self, bz: str | int | float | types.Real) -> None:
        """
        Sets `bz`.

        Parameters:
            bz: Polyhedron corner #2 z component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if bz is not None:
            if isinstance(bz, types.Real):
                bz = bz
            elif isinstance(bz, int) or isinstance(bz, float):
                bz = types.Real(bz)
            elif isinstance(bz, str):
                bz = types.Real.from_mcnp(bz)

        if bz is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bz)

        self._bz: types.Real = bz

    @property
    def cx(self) -> types.Real:
        """
        Polyhedron corner #3 x component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._cx

    @cx.setter
    def cx(self, cx: str | int | float | types.Real) -> None:
        """
        Sets `cx`.

        Parameters:
            cx: Polyhedron corner #3 x component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if cx is not None:
            if isinstance(cx, types.Real):
                cx = cx
            elif isinstance(cx, int) or isinstance(cx, float):
                cx = types.Real(cx)
            elif isinstance(cx, str):
                cx = types.Real.from_mcnp(cx)

        if cx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, cx)

        self._cx: types.Real = cx

    @property
    def cy(self) -> types.Real:
        """
        Polyhedron corner #3 y component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._cy

    @cy.setter
    def cy(self, cy: str | int | float | types.Real) -> None:
        """
        Sets `cy`.

        Parameters:
            cy: Polyhedron corner #3 y component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if cy is not None:
            if isinstance(cy, types.Real):
                cy = cy
            elif isinstance(cy, int) or isinstance(cy, float):
                cy = types.Real(cy)
            elif isinstance(cy, str):
                cy = types.Real.from_mcnp(cy)

        if cy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, cy)

        self._cy: types.Real = cy

    @property
    def cz(self) -> types.Real:
        """
        Polyhedron corner #3 z component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._cz

    @cz.setter
    def cz(self, cz: str | int | float | types.Real) -> None:
        """
        Sets `cz`.

        Parameters:
            cz: Polyhedron corner #3 z component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if cz is not None:
            if isinstance(cz, types.Real):
                cz = cz
            elif isinstance(cz, int) or isinstance(cz, float):
                cz = types.Real(cz)
            elif isinstance(cz, str):
                cz = types.Real.from_mcnp(cz)

        if cz is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, cz)

        self._cz: types.Real = cz

    @property
    def dx(self) -> types.Real:
        """
        Polyhedron corner #4 x component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._dx

    @dx.setter
    def dx(self, dx: str | int | float | types.Real) -> None:
        """
        Sets `dx`.

        Parameters:
            dx: Polyhedron corner #4 x component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if dx is not None:
            if isinstance(dx, types.Real):
                dx = dx
            elif isinstance(dx, int) or isinstance(dx, float):
                dx = types.Real(dx)
            elif isinstance(dx, str):
                dx = types.Real.from_mcnp(dx)

        if dx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, dx)

        self._dx: types.Real = dx

    @property
    def dy(self) -> types.Real:
        """
        Polyhedron corner #4 y component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._dy

    @dy.setter
    def dy(self, dy: str | int | float | types.Real) -> None:
        """
        Sets `dy`.

        Parameters:
            dy: Polyhedron corner #4 y component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if dy is not None:
            if isinstance(dy, types.Real):
                dy = dy
            elif isinstance(dy, int) or isinstance(dy, float):
                dy = types.Real(dy)
            elif isinstance(dy, str):
                dy = types.Real.from_mcnp(dy)

        if dy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, dy)

        self._dy: types.Real = dy

    @property
    def dz(self) -> types.Real:
        """
        Polyhedron corner #4 z component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._dz

    @dz.setter
    def dz(self, dz: str | int | float | types.Real) -> None:
        """
        Sets `dz`.

        Parameters:
            dz: Polyhedron corner #4 z component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if dz is not None:
            if isinstance(dz, types.Real):
                dz = dz
            elif isinstance(dz, int) or isinstance(dz, float):
                dz = types.Real(dz)
            elif isinstance(dz, str):
                dz = types.Real.from_mcnp(dz)

        if dz is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, dz)

        self._dz: types.Real = dz

    @property
    def ex(self) -> types.Real:
        """
        Polyhedron corner #5 x component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._ex

    @ex.setter
    def ex(self, ex: str | int | float | types.Real) -> None:
        """
        Sets `ex`.

        Parameters:
            ex: Polyhedron corner #5 x component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if ex is not None:
            if isinstance(ex, types.Real):
                ex = ex
            elif isinstance(ex, int) or isinstance(ex, float):
                ex = types.Real(ex)
            elif isinstance(ex, str):
                ex = types.Real.from_mcnp(ex)

        if ex is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ex)

        self._ex: types.Real = ex

    @property
    def ey(self) -> types.Real:
        """
        Polyhedron corner #5 y component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._ey

    @ey.setter
    def ey(self, ey: str | int | float | types.Real) -> None:
        """
        Sets `ey`.

        Parameters:
            ey: Polyhedron corner #5 y component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if ey is not None:
            if isinstance(ey, types.Real):
                ey = ey
            elif isinstance(ey, int) or isinstance(ey, float):
                ey = types.Real(ey)
            elif isinstance(ey, str):
                ey = types.Real.from_mcnp(ey)

        if ey is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ey)

        self._ey: types.Real = ey

    @property
    def ez(self) -> types.Real:
        """
        Polyhedron corner #5 z component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._ez

    @ez.setter
    def ez(self, ez: str | int | float | types.Real) -> None:
        """
        Sets `ez`.

        Parameters:
            ez: Polyhedron corner #5 z component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if ez is not None:
            if isinstance(ez, types.Real):
                ez = ez
            elif isinstance(ez, int) or isinstance(ez, float):
                ez = types.Real(ez)
            elif isinstance(ez, str):
                ez = types.Real.from_mcnp(ez)

        if ez is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ez)

        self._ez: types.Real = ez

    @property
    def fx(self) -> types.Real:
        """
        Polyhedron corner #6 x component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._fx

    @fx.setter
    def fx(self, fx: str | int | float | types.Real) -> None:
        """
        Sets `fx`.

        Parameters:
            fx: Polyhedron corner #6 x component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if fx is not None:
            if isinstance(fx, types.Real):
                fx = fx
            elif isinstance(fx, int) or isinstance(fx, float):
                fx = types.Real(fx)
            elif isinstance(fx, str):
                fx = types.Real.from_mcnp(fx)

        if fx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, fx)

        self._fx: types.Real = fx

    @property
    def fy(self) -> types.Real:
        """
        Polyhedron corner #6 y component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._fy

    @fy.setter
    def fy(self, fy: str | int | float | types.Real) -> None:
        """
        Sets `fy`.

        Parameters:
            fy: Polyhedron corner #6 y component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if fy is not None:
            if isinstance(fy, types.Real):
                fy = fy
            elif isinstance(fy, int) or isinstance(fy, float):
                fy = types.Real(fy)
            elif isinstance(fy, str):
                fy = types.Real.from_mcnp(fy)

        if fy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, fy)

        self._fy: types.Real = fy

    @property
    def fz(self) -> types.Real:
        """
        Polyhedron corner #6 z component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._fz

    @fz.setter
    def fz(self, fz: str | int | float | types.Real) -> None:
        """
        Sets `fz`.

        Parameters:
            fz: Polyhedron corner #6 z component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if fz is not None:
            if isinstance(fz, types.Real):
                fz = fz
            elif isinstance(fz, int) or isinstance(fz, float):
                fz = types.Real(fz)
            elif isinstance(fz, str):
                fz = types.Real.from_mcnp(fz)

        if fz is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, fz)

        self._fz: types.Real = fz

    @property
    def gx(self) -> types.Real:
        """
        Polyhedron corner #7 x component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._gx

    @gx.setter
    def gx(self, gx: str | int | float | types.Real) -> None:
        """
        Sets `gx`.

        Parameters:
            gx: Polyhedron corner #7 x component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if gx is not None:
            if isinstance(gx, types.Real):
                gx = gx
            elif isinstance(gx, int) or isinstance(gx, float):
                gx = types.Real(gx)
            elif isinstance(gx, str):
                gx = types.Real.from_mcnp(gx)

        if gx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, gx)

        self._gx: types.Real = gx

    @property
    def gy(self) -> types.Real:
        """
        Polyhedron corner #7 y component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._gy

    @gy.setter
    def gy(self, gy: str | int | float | types.Real) -> None:
        """
        Sets `gy`.

        Parameters:
            gy: Polyhedron corner #7 y component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if gy is not None:
            if isinstance(gy, types.Real):
                gy = gy
            elif isinstance(gy, int) or isinstance(gy, float):
                gy = types.Real(gy)
            elif isinstance(gy, str):
                gy = types.Real.from_mcnp(gy)

        if gy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, gy)

        self._gy: types.Real = gy

    @property
    def gz(self) -> types.Real:
        """
        Polyhedron corner #7 z component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._gz

    @gz.setter
    def gz(self, gz: str | int | float | types.Real) -> None:
        """
        Sets `gz`.

        Parameters:
            gz: Polyhedron corner #7 z component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if gz is not None:
            if isinstance(gz, types.Real):
                gz = gz
            elif isinstance(gz, int) or isinstance(gz, float):
                gz = types.Real(gz)
            elif isinstance(gz, str):
                gz = types.Real.from_mcnp(gz)

        if gz is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, gz)

        self._gz: types.Real = gz

    @property
    def hx(self) -> types.Real:
        """
        Polyhedron corner #8 x component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._hx

    @hx.setter
    def hx(self, hx: str | int | float | types.Real) -> None:
        """
        Sets `hx`.

        Parameters:
            hx: Polyhedron corner #8 x component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if hx is not None:
            if isinstance(hx, types.Real):
                hx = hx
            elif isinstance(hx, int) or isinstance(hx, float):
                hx = types.Real(hx)
            elif isinstance(hx, str):
                hx = types.Real.from_mcnp(hx)

        if hx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, hx)

        self._hx: types.Real = hx

    @property
    def hy(self) -> types.Real:
        """
        Polyhedron corner #8 y component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._hy

    @hy.setter
    def hy(self, hy: str | int | float | types.Real) -> None:
        """
        Sets `hy`.

        Parameters:
            hy: Polyhedron corner #8 y component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if hy is not None:
            if isinstance(hy, types.Real):
                hy = hy
            elif isinstance(hy, int) or isinstance(hy, float):
                hy = types.Real(hy)
            elif isinstance(hy, str):
                hy = types.Real.from_mcnp(hy)

        if hy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, hy)

        self._hy: types.Real = hy

    @property
    def hz(self) -> types.Real:
        """
        Polyhedron corner #8 z component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._hz

    @hz.setter
    def hz(self, hz: str | int | float | types.Real) -> None:
        """
        Sets `hz`.

        Parameters:
            hz: Polyhedron corner #8 z component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if hz is not None:
            if isinstance(hz, types.Real):
                hz = hz
            elif isinstance(hz, int) or isinstance(hz, float):
                hz = types.Real(hz)
            elif isinstance(hz, str):
                hz = types.Real.from_mcnp(hz)

        if hz is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, hz)

        self._hz: types.Real = hz

    @property
    def n1(self) -> types.Real:
        """
        Polyhedron four-digit side specificer #1

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._n1

    @n1.setter
    def n1(self, n1: str | int | float | types.Real) -> None:
        """
        Sets `n1`.

        Parameters:
            n1: Polyhedron four-digit side specificer #1.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if n1 is not None:
            if isinstance(n1, types.Real):
                n1 = n1
            elif isinstance(n1, int) or isinstance(n1, float):
                n1 = types.Real(n1)
            elif isinstance(n1, str):
                n1 = types.Real.from_mcnp(n1)

        if n1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, n1)

        self._n1: types.Real = n1

    @property
    def n2(self) -> types.Real:
        """
        Polyhedron four-digit side specificer #2

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._n2

    @n2.setter
    def n2(self, n2: str | int | float | types.Real) -> None:
        """
        Sets `n2`.

        Parameters:
            n2: Polyhedron four-digit side specificer #2.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if n2 is not None:
            if isinstance(n2, types.Real):
                n2 = n2
            elif isinstance(n2, int) or isinstance(n2, float):
                n2 = types.Real(n2)
            elif isinstance(n2, str):
                n2 = types.Real.from_mcnp(n2)

        if n2 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, n2)

        self._n2: types.Real = n2

    @property
    def n3(self) -> types.Real:
        """
        Polyhedron four-digit side specificer #3

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._n3

    @n3.setter
    def n3(self, n3: str | int | float | types.Real) -> None:
        """
        Sets `n3`.

        Parameters:
            n3: Polyhedron four-digit side specificer #3.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if n3 is not None:
            if isinstance(n3, types.Real):
                n3 = n3
            elif isinstance(n3, int) or isinstance(n3, float):
                n3 = types.Real(n3)
            elif isinstance(n3, str):
                n3 = types.Real.from_mcnp(n3)

        if n3 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, n3)

        self._n3: types.Real = n3

    @property
    def n4(self) -> types.Real:
        """
        Polyhedron four-digit side specificer #4

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._n4

    @n4.setter
    def n4(self, n4: str | int | float | types.Real) -> None:
        """
        Sets `n4`.

        Parameters:
            n4: Polyhedron four-digit side specificer #4.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if n4 is not None:
            if isinstance(n4, types.Real):
                n4 = n4
            elif isinstance(n4, int) or isinstance(n4, float):
                n4 = types.Real(n4)
            elif isinstance(n4, str):
                n4 = types.Real.from_mcnp(n4)

        if n4 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, n4)

        self._n4: types.Real = n4

    @property
    def n5(self) -> types.Real:
        """
        Polyhedron four-digit side specificer #5

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._n5

    @n5.setter
    def n5(self, n5: str | int | float | types.Real) -> None:
        """
        Sets `n5`.

        Parameters:
            n5: Polyhedron four-digit side specificer #5.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if n5 is not None:
            if isinstance(n5, types.Real):
                n5 = n5
            elif isinstance(n5, int) or isinstance(n5, float):
                n5 = types.Real(n5)
            elif isinstance(n5, str):
                n5 = types.Real.from_mcnp(n5)

        if n5 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, n5)

        self._n5: types.Real = n5

    @property
    def n6(self) -> types.Real:
        """
        Polyhedron four-digit side specificer #6

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._n6

    @n6.setter
    def n6(self, n6: str | int | float | types.Real) -> None:
        """
        Sets `n6`.

        Parameters:
            n6: Polyhedron four-digit side specificer #6.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if n6 is not None:
            if isinstance(n6, types.Real):
                n6 = n6
            elif isinstance(n6, int) or isinstance(n6, float):
                n6 = types.Real(n6)
            elif isinstance(n6, str):
                n6 = types.Real.from_mcnp(n6)

        if n6 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, n6)

        self._n6: types.Real = n6
