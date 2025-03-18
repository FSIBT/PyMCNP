import re
import typing


from .option_ import SurfaceOption_
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class Rpp(SurfaceOption_, keyword='rpp'):
    """
    Represents INP rpp elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
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
        rf'rpp( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})'
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
