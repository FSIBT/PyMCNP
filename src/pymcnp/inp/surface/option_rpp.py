import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser
from ...utils import _visualization


class SurfaceOption_Rpp(_option.SurfaceOption_, keyword='rpp'):
    """
    Represents INP surface card rpp options.

    Attributes:
        xmin: Parallelepiped x termini minimum.
        xmax: Parallelepiped x termini maximum.
        ymin: Parallelepiped y termini minimum.
        ymax: Parallelepiped y termini maximum.
        zmin: Parallelepiped z termini minimum.
        zmax: Parallelepiped z termini maximum.
    """

    _REGEX = re.compile(r'\Arpp( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)\Z')

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
        Initializes ``SurfaceOption_Rpp``.

        Parameters:
            xmin: Parallelepiped x termini minimum.
            xmax: Parallelepiped x termini maximum.
            ymin: Parallelepiped y termini minimum.
            ymax: Parallelepiped y termini maximum.
            zmin: Parallelepiped z termini minimum.
            zmax: Parallelepiped z termini maximum.

        Returns:
            ``SurfaceOption_Rpp``.

        Raises:
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
        """

        if xmin is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, xmin)
        if xmax is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, xmax)
        if ymin is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, ymin)
        if ymax is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, ymax)
        if zmin is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, zmin)
        if zmax is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, zmax)

        self.value: typing.Final[tuple[any]] = types._Tuple([xmin, xmax, ymin, ymax, zmin, zmax])
        self.xmin: typing.Final[types.Real] = xmin
        self.xmax: typing.Final[types.Real] = xmax
        self.ymin: typing.Final[types.Real] = ymin
        self.ymax: typing.Final[types.Real] = ymax
        self.zmin: typing.Final[types.Real] = zmin
        self.zmax: typing.Final[types.Real] = zmax

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SurfaceOption_Rpp`` from INP.

        Parameters:
            source: INP surface card option.

        Returns:
            ``SurfaceOption_Rpp``.

        Raises:
            McnpError: SYNTAX_SURFACE_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SurfaceOption_Rpp._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_SURFACE_OPTION, source)

        xmin = types.Real.from_mcnp(tokens[1])
        xmax = types.Real.from_mcnp(tokens[2])
        ymin = types.Real.from_mcnp(tokens[3])
        ymax = types.Real.from_mcnp(tokens[4])
        zmin = types.Real.from_mcnp(tokens[5])
        zmax = types.Real.from_mcnp(tokens[6])

        return SurfaceOption_Rpp(xmin, xmax, ymin, ymax, zmin, zmax)

    def to_pyvista(self):
        """
        Generates ``pyvista.PolyData`` from ``SurfaceOption_Rpp``.

        Returns:
            ``pyvista.PolyData`` for ``SurfaceOption_Rpp``
        """

        vis = _visualization.McnpVisualization.get_parallelipiped(
            self.xmin.value,
            self.xmax.value,
            self.ymin.value,
            self.ymax.value,
            self.zmin.value,
            self.zmax.value,
        )

        return vis.data
