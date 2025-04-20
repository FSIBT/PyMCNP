import re
import typing
import dataclasses


from .option_ import SurfaceOption_
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class Rpp(SurfaceOption_, keyword='rpp'):
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

    _ATTRS = {
        'xmin': types.Real,
        'xmax': types.Real,
        'ymin': types.Real,
        'ymax': types.Real,
        'zmin': types.Real,
        'zmax': types.Real,
    }

    _REGEX = re.compile(
        rf'\Arpp( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})\Z'
    )

    def __init__(
        self,
        xmin: types.Real,
        xmax: types.Real,
        ymin: types.Real,
        ymax: types.Real,
        zmin: types.Real,
        zmax: types.Real,
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
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if xmin is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, xmin)
        if xmax is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, xmax)
        if ymin is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ymin)
        if ymax is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ymax)
        if zmin is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, zmin)
        if zmax is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, zmax)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                xmin,
                xmax,
                ymin,
                ymax,
                zmin,
                zmax,
            ]
        )

        self.xmin: typing.Final[types.Real] = xmin
        self.xmax: typing.Final[types.Real] = xmax
        self.ymin: typing.Final[types.Real] = ymin
        self.ymax: typing.Final[types.Real] = ymax
        self.zmin: typing.Final[types.Real] = zmin
        self.zmax: typing.Final[types.Real] = zmax

    def draw(self):
        """
        Generates ``Visualization`` from ``Rpp``.

        Returns:
            ``pyvista.PolyData`` for ``Rpp``
        """

        vis = _visualization.Visualization.get_parallelipiped(
            self.xmin.value,
            self.xmax.value,
            self.ymin.value,
            self.ymax.value,
            self.zmin.value,
            self.zmax.value,
        )

        return vis


@dataclasses.dataclass
class RppBuilder:
    """
    Builds ``Rpp``.

    Attributes:
        xmin: Parallelepiped x termini minimum.
        xmax: Parallelepiped x termini maximum.
        ymin: Parallelepiped y termini minimum.
        ymax: Parallelepiped y termini maximum.
        zmin: Parallelepiped z termini minimum.
        zmax: Parallelepiped z termini maximum.
    """

    xmin: str | float | types.Real
    xmax: str | float | types.Real
    ymin: str | float | types.Real
    ymax: str | float | types.Real
    zmin: str | float | types.Real
    zmax: str | float | types.Real

    def build(self):
        """
        Builds ``RppBuilder`` into ``Rpp``.

        Returns:
            ``Rpp`` for ``RppBuilder``.
        """

        if isinstance(self.xmin, types.Real):
            xmin = self.xmin
        elif isinstance(self.xmin, float) or isinstance(self.xmin, int):
            xmin = types.Real(self.xmin)
        elif isinstance(self.xmin, str):
            xmin = types.Real.from_mcnp(self.xmin)

        if isinstance(self.xmax, types.Real):
            xmax = self.xmax
        elif isinstance(self.xmax, float) or isinstance(self.xmax, int):
            xmax = types.Real(self.xmax)
        elif isinstance(self.xmax, str):
            xmax = types.Real.from_mcnp(self.xmax)

        if isinstance(self.ymin, types.Real):
            ymin = self.ymin
        elif isinstance(self.ymin, float) or isinstance(self.ymin, int):
            ymin = types.Real(self.ymin)
        elif isinstance(self.ymin, str):
            ymin = types.Real.from_mcnp(self.ymin)

        if isinstance(self.ymax, types.Real):
            ymax = self.ymax
        elif isinstance(self.ymax, float) or isinstance(self.ymax, int):
            ymax = types.Real(self.ymax)
        elif isinstance(self.ymax, str):
            ymax = types.Real.from_mcnp(self.ymax)

        if isinstance(self.zmin, types.Real):
            zmin = self.zmin
        elif isinstance(self.zmin, float) or isinstance(self.zmin, int):
            zmin = types.Real(self.zmin)
        elif isinstance(self.zmin, str):
            zmin = types.Real.from_mcnp(self.zmin)

        if isinstance(self.zmax, types.Real):
            zmax = self.zmax
        elif isinstance(self.zmax, float) or isinstance(self.zmax, int):
            zmax = types.Real(self.zmax)
        elif isinstance(self.zmax, str):
            zmax = types.Real.from_mcnp(self.zmax)

        return Rpp(
            xmin=xmin,
            xmax=xmax,
            ymin=ymin,
            ymax=ymax,
            zmin=zmin,
            zmax=zmax,
        )
