import re

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class Rpp(_option.SurfaceOption):
    """
    Represents INP rpp elements.

    Attributes:
        xmin: Parallelepiped x termini minimum.
        xmax: Parallelepiped x termini maximum.
        ymin: Parallelepiped y termini minimum.
        ymax: Parallelepiped y termini maximum.
        zmin: Parallelepiped z termini minimum.
        zmax: Parallelepiped z termini maximum.
    """

    _KEYWORD = 'rpp'

    _ATTRS = {
        'xmin': types.Real,
        'xmax': types.Real,
        'ymin': types.Real,
        'ymax': types.Real,
        'zmin': types.Real,
        'zmax': types.Real,
    }

    _REGEX = re.compile(
        rf'\Arpp( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?\Z'
    )

    def __init__(
        self,
        xmin: str | int | float | types.Real,
        xmax: str | int | float | types.Real,
        ymin: str | int | float | types.Real,
        ymax: str | int | float | types.Real,
        zmin: str | int | float | types.Real = None,
        zmax: str | int | float | types.Real = None,
    ):
        """
        Initializes ``Rpp``.

        Parameters:
            xmin: Parallelepiped x termini minimum.
            xmax: Parallelepiped x termini maximum.
            ymin: Parallelepiped y termini minimum.
            ymax: Parallelepiped y termini maximum.
            zmin: Parallelepiped z termini minimum.
            zmax: Parallelepiped z termini maximum.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.xmin: types.Real = xmin
        self.xmax: types.Real = xmax
        self.ymin: types.Real = ymin
        self.ymax: types.Real = ymax
        self.zmin: types.Real = zmin
        self.zmax: types.Real = zmax

    @property
    def xmin(self) -> types.Real:
        """
        Gets ``xmin``.

        Returns:
            ``xmin``.
        """

        return self._xmin

    @xmin.setter
    def xmin(self, xmin: str | int | float | types.Real) -> None:
        """
        Sets ``xmin``.

        Parameters:
            xmin: Parallelepiped x termini minimum.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if xmin is not None:
            if isinstance(xmin, types.Real):
                xmin = xmin
            elif isinstance(xmin, int):
                xmin = types.Real(xmin)
            elif isinstance(xmin, float):
                xmin = types.Real(xmin)
            elif isinstance(xmin, str):
                xmin = types.Real.from_mcnp(xmin)
            else:
                raise TypeError

        if xmin is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, xmin)

        self._xmin: types.Real = xmin

    @property
    def xmax(self) -> types.Real:
        """
        Gets ``xmax``.

        Returns:
            ``xmax``.
        """

        return self._xmax

    @xmax.setter
    def xmax(self, xmax: str | int | float | types.Real) -> None:
        """
        Sets ``xmax``.

        Parameters:
            xmax: Parallelepiped x termini maximum.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if xmax is not None:
            if isinstance(xmax, types.Real):
                xmax = xmax
            elif isinstance(xmax, int):
                xmax = types.Real(xmax)
            elif isinstance(xmax, float):
                xmax = types.Real(xmax)
            elif isinstance(xmax, str):
                xmax = types.Real.from_mcnp(xmax)
            else:
                raise TypeError

        if xmax is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, xmax)

        self._xmax: types.Real = xmax

    @property
    def ymin(self) -> types.Real:
        """
        Gets ``ymin``.

        Returns:
            ``ymin``.
        """

        return self._ymin

    @ymin.setter
    def ymin(self, ymin: str | int | float | types.Real) -> None:
        """
        Sets ``ymin``.

        Parameters:
            ymin: Parallelepiped y termini minimum.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if ymin is not None:
            if isinstance(ymin, types.Real):
                ymin = ymin
            elif isinstance(ymin, int):
                ymin = types.Real(ymin)
            elif isinstance(ymin, float):
                ymin = types.Real(ymin)
            elif isinstance(ymin, str):
                ymin = types.Real.from_mcnp(ymin)
            else:
                raise TypeError

        if ymin is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ymin)

        self._ymin: types.Real = ymin

    @property
    def ymax(self) -> types.Real:
        """
        Gets ``ymax``.

        Returns:
            ``ymax``.
        """

        return self._ymax

    @ymax.setter
    def ymax(self, ymax: str | int | float | types.Real) -> None:
        """
        Sets ``ymax``.

        Parameters:
            ymax: Parallelepiped y termini maximum.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if ymax is not None:
            if isinstance(ymax, types.Real):
                ymax = ymax
            elif isinstance(ymax, int):
                ymax = types.Real(ymax)
            elif isinstance(ymax, float):
                ymax = types.Real(ymax)
            elif isinstance(ymax, str):
                ymax = types.Real.from_mcnp(ymax)
            else:
                raise TypeError

        if ymax is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ymax)

        self._ymax: types.Real = ymax

    @property
    def zmin(self) -> types.Real:
        """
        Gets ``zmin``.

        Returns:
            ``zmin``.
        """

        return self._zmin

    @zmin.setter
    def zmin(self, zmin: str | int | float | types.Real) -> None:
        """
        Sets ``zmin``.

        Parameters:
            zmin: Parallelepiped z termini minimum.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if zmin is not None:
            if isinstance(zmin, types.Real):
                zmin = zmin
            elif isinstance(zmin, int):
                zmin = types.Real(zmin)
            elif isinstance(zmin, float):
                zmin = types.Real(zmin)
            elif isinstance(zmin, str):
                zmin = types.Real.from_mcnp(zmin)
            else:
                raise TypeError

        self._zmin: types.Real = zmin

    @property
    def zmax(self) -> types.Real:
        """
        Gets ``zmax``.

        Returns:
            ``zmax``.
        """

        return self._zmax

    @zmax.setter
    def zmax(self, zmax: str | int | float | types.Real) -> None:
        """
        Sets ``zmax``.

        Parameters:
            zmax: Parallelepiped z termini maximum.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if zmax is not None:
            if isinstance(zmax, types.Real):
                zmax = zmax
            elif isinstance(zmax, int):
                zmax = types.Real(zmax)
            elif isinstance(zmax, float):
                zmax = types.Real(zmax)
            elif isinstance(zmax, str):
                zmax = types.Real.from_mcnp(zmax)
            else:
                raise TypeError

        self._zmax: types.Real = zmax

    def draw(self):
        """
        Generates ``Visualization`` from ``Rpp``.

        Returns:
            ``pyvista.PolyData`` for ``Rpp``
        """

        vis = _visualization.Visualization.get_parallelipiped(
            float(self.xmin),
            float(self.xmax),
            float(self.ymin),
            float(self.ymax),
            float(self.zmin),
            float(self.zmax),
        )

        return vis
