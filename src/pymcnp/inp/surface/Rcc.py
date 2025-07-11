import re

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class Rcc(_option.SurfaceOption):
    """
    Represents INP rcc elements.

    Attributes:
        vx: Circular cylinder macrobody position vector x component.
        vy: Circular cylinder macrobody position vector y component.
        vz: Circular cylinder macrobody position vector z component.
        hx: Circular cylinder macrobody height vector x component.
        hy: Circular cylinder macrobody height vector y component.
        hz: Circular cylinder macrobody height vector z component.
        r: Circular cylinder macrobody radius.
    """

    _KEYWORD = 'rcc'

    _ATTRS = {
        'vx': types.Real,
        'vy': types.Real,
        'vz': types.Real,
        'hx': types.Real,
        'hy': types.Real,
        'hz': types.Real,
        'r': types.Real,
    }

    _REGEX = re.compile(
        rf'\Arcc( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z'
    )

    def __init__(
        self,
        vx: str | int | float | types.Real,
        vy: str | int | float | types.Real,
        vz: str | int | float | types.Real,
        hx: str | int | float | types.Real,
        hy: str | int | float | types.Real,
        hz: str | int | float | types.Real,
        r: str | int | float | types.Real,
    ):
        """
        Initializes ``Rcc``.

        Parameters:
            vx: Circular cylinder macrobody position vector x component.
            vy: Circular cylinder macrobody position vector y component.
            vz: Circular cylinder macrobody position vector z component.
            hx: Circular cylinder macrobody height vector x component.
            hy: Circular cylinder macrobody height vector y component.
            hz: Circular cylinder macrobody height vector z component.
            r: Circular cylinder macrobody radius.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.vx: types.Real = vx
        self.vy: types.Real = vy
        self.vz: types.Real = vz
        self.hx: types.Real = hx
        self.hy: types.Real = hy
        self.hz: types.Real = hz
        self.r: types.Real = r

    @property
    def vx(self) -> types.Real:
        """
        Gets ``vx``.

        Returns:
            ``vx``.
        """

        return self._vx

    @vx.setter
    def vx(self, vx: str | int | float | types.Real) -> None:
        """
        Sets ``vx``.

        Parameters:
            vx: Circular cylinder macrobody position vector x component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if vx is not None:
            if isinstance(vx, types.Real):
                vx = vx
            elif isinstance(vx, int):
                vx = types.Real(vx)
            elif isinstance(vx, float):
                vx = types.Real(vx)
            elif isinstance(vx, str):
                vx = types.Real.from_mcnp(vx)
            else:
                raise TypeError

        if vx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, vx)

        self._vx: types.Real = vx

    @property
    def vy(self) -> types.Real:
        """
        Gets ``vy``.

        Returns:
            ``vy``.
        """

        return self._vy

    @vy.setter
    def vy(self, vy: str | int | float | types.Real) -> None:
        """
        Sets ``vy``.

        Parameters:
            vy: Circular cylinder macrobody position vector y component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if vy is not None:
            if isinstance(vy, types.Real):
                vy = vy
            elif isinstance(vy, int):
                vy = types.Real(vy)
            elif isinstance(vy, float):
                vy = types.Real(vy)
            elif isinstance(vy, str):
                vy = types.Real.from_mcnp(vy)
            else:
                raise TypeError

        if vy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, vy)

        self._vy: types.Real = vy

    @property
    def vz(self) -> types.Real:
        """
        Gets ``vz``.

        Returns:
            ``vz``.
        """

        return self._vz

    @vz.setter
    def vz(self, vz: str | int | float | types.Real) -> None:
        """
        Sets ``vz``.

        Parameters:
            vz: Circular cylinder macrobody position vector z component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if vz is not None:
            if isinstance(vz, types.Real):
                vz = vz
            elif isinstance(vz, int):
                vz = types.Real(vz)
            elif isinstance(vz, float):
                vz = types.Real(vz)
            elif isinstance(vz, str):
                vz = types.Real.from_mcnp(vz)
            else:
                raise TypeError

        if vz is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, vz)

        self._vz: types.Real = vz

    @property
    def hx(self) -> types.Real:
        """
        Gets ``hx``.

        Returns:
            ``hx``.
        """

        return self._hx

    @hx.setter
    def hx(self, hx: str | int | float | types.Real) -> None:
        """
        Sets ``hx``.

        Parameters:
            hx: Circular cylinder macrobody height vector x component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if hx is not None:
            if isinstance(hx, types.Real):
                hx = hx
            elif isinstance(hx, int):
                hx = types.Real(hx)
            elif isinstance(hx, float):
                hx = types.Real(hx)
            elif isinstance(hx, str):
                hx = types.Real.from_mcnp(hx)
            else:
                raise TypeError

        if hx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, hx)

        self._hx: types.Real = hx

    @property
    def hy(self) -> types.Real:
        """
        Gets ``hy``.

        Returns:
            ``hy``.
        """

        return self._hy

    @hy.setter
    def hy(self, hy: str | int | float | types.Real) -> None:
        """
        Sets ``hy``.

        Parameters:
            hy: Circular cylinder macrobody height vector y component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if hy is not None:
            if isinstance(hy, types.Real):
                hy = hy
            elif isinstance(hy, int):
                hy = types.Real(hy)
            elif isinstance(hy, float):
                hy = types.Real(hy)
            elif isinstance(hy, str):
                hy = types.Real.from_mcnp(hy)
            else:
                raise TypeError

        if hy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, hy)

        self._hy: types.Real = hy

    @property
    def hz(self) -> types.Real:
        """
        Gets ``hz``.

        Returns:
            ``hz``.
        """

        return self._hz

    @hz.setter
    def hz(self, hz: str | int | float | types.Real) -> None:
        """
        Sets ``hz``.

        Parameters:
            hz: Circular cylinder macrobody height vector z component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if hz is not None:
            if isinstance(hz, types.Real):
                hz = hz
            elif isinstance(hz, int):
                hz = types.Real(hz)
            elif isinstance(hz, float):
                hz = types.Real(hz)
            elif isinstance(hz, str):
                hz = types.Real.from_mcnp(hz)
            else:
                raise TypeError

        if hz is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, hz)

        self._hz: types.Real = hz

    @property
    def r(self) -> types.Real:
        """
        Gets ``r``.

        Returns:
            ``r``.
        """

        return self._r

    @r.setter
    def r(self, r: str | int | float | types.Real) -> None:
        """
        Sets ``r``.

        Parameters:
            r: Circular cylinder macrobody radius.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if r is not None:
            if isinstance(r, types.Real):
                r = r
            elif isinstance(r, int):
                r = types.Real(r)
            elif isinstance(r, float):
                r = types.Real(r)
            elif isinstance(r, str):
                r = types.Real.from_mcnp(r)
            else:
                raise TypeError

        if r is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, r)

        self._r: types.Real = r

    def draw(self):
        """
        Generates ``Visualization`` from ``Rcc``.

        Returns:
            ``pyvista.PolyData`` for ``Rcc``
        """

        v = _visualization.Vector(self.vx, self.vy, self.vz)
        h = _visualization.Vector(self.hx, self.hy, self.hz)

        cross = v * _visualization.Vector(0, 0, 1)
        angle = v & _visualization.Vector(0, 0, 1)

        vis = _visualization.Visualization.get_cylinder_circle(h.norm(), self.r)
        vis = vis.add_rotation(cross, angle, (0, 0, 0))
        vis = vis.add_translation(v)

        return vis
