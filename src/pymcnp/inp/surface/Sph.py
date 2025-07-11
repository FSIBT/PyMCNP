import re

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class Sph(_option.SurfaceOption):
    """
    Represents INP sph elements.

    Attributes:
        vx: Sphere macrobody position vector x component.
        vy: Sphere macrobody position vector y component.
        vz: Sphere macrobody position vector z component.
        r: Sphere macrobody radius.
    """

    _KEYWORD = 'sph'

    _ATTRS = {
        'vx': types.Real,
        'vy': types.Real,
        'vz': types.Real,
        'r': types.Real,
    }

    _REGEX = re.compile(rf'\Asph( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, vx: str | int | float | types.Real, vy: str | int | float | types.Real, vz: str | int | float | types.Real, r: str | int | float | types.Real):
        """
        Initializes ``Sph``.

        Parameters:
            vx: Sphere macrobody position vector x component.
            vy: Sphere macrobody position vector y component.
            vz: Sphere macrobody position vector z component.
            r: Sphere macrobody radius.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.vx: types.Real = vx
        self.vy: types.Real = vy
        self.vz: types.Real = vz
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
            vx: Sphere macrobody position vector x component.

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
            vy: Sphere macrobody position vector y component.

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
            vz: Sphere macrobody position vector z component.

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
            r: Sphere macrobody radius.

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
        Generates ``Visualization`` from ``Sph``.

        Returns:
            ``pyvista.PolyData`` for ``Sph``
        """

        vis = _visualization.Visualization.get_sphere(float(self.r))
        vis = vis.add_translation(_visualization.Vector(self.vx, self.vy, self.vz))

        return vis
