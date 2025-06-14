import re
import copy
import typing
import dataclasses


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

    def __init__(self, xmin: types.Real, xmax: types.Real, ymin: types.Real, ymax: types.Real, zmin: types.Real = None, zmax: types.Real = None):
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

        if xmin is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, xmin)
        if xmax is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, xmax)
        if ymin is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ymin)
        if ymax is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ymax)

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
class RppBuilder(_option.SurfaceOptionBuilder):
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
    zmin: str | float | types.Real = None
    zmax: str | float | types.Real = None

    def build(self):
        """
        Builds ``RppBuilder`` into ``Rpp``.

        Returns:
            ``Rpp`` for ``RppBuilder``.
        """

        xmin = self.xmin
        if isinstance(self.xmin, types.Real):
            xmin = self.xmin
        elif isinstance(self.xmin, float) or isinstance(self.xmin, int):
            xmin = types.Real(self.xmin)
        elif isinstance(self.xmin, str):
            xmin = types.Real.from_mcnp(self.xmin)

        xmax = self.xmax
        if isinstance(self.xmax, types.Real):
            xmax = self.xmax
        elif isinstance(self.xmax, float) or isinstance(self.xmax, int):
            xmax = types.Real(self.xmax)
        elif isinstance(self.xmax, str):
            xmax = types.Real.from_mcnp(self.xmax)

        ymin = self.ymin
        if isinstance(self.ymin, types.Real):
            ymin = self.ymin
        elif isinstance(self.ymin, float) or isinstance(self.ymin, int):
            ymin = types.Real(self.ymin)
        elif isinstance(self.ymin, str):
            ymin = types.Real.from_mcnp(self.ymin)

        ymax = self.ymax
        if isinstance(self.ymax, types.Real):
            ymax = self.ymax
        elif isinstance(self.ymax, float) or isinstance(self.ymax, int):
            ymax = types.Real(self.ymax)
        elif isinstance(self.ymax, str):
            ymax = types.Real.from_mcnp(self.ymax)

        zmin = self.zmin
        if isinstance(self.zmin, types.Real):
            zmin = self.zmin
        elif isinstance(self.zmin, float) or isinstance(self.zmin, int):
            zmin = types.Real(self.zmin)
        elif isinstance(self.zmin, str):
            zmin = types.Real.from_mcnp(self.zmin)

        zmax = self.zmax
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

    @staticmethod
    def unbuild(ast: Rpp):
        """
        Unbuilds ``Rpp`` into ``RppBuilder``

        Returns:
            ``RppBuilder`` for ``Rpp``.
        """

        return RppBuilder(
            xmin=copy.deepcopy(ast.xmin),
            xmax=copy.deepcopy(ast.xmax),
            ymin=copy.deepcopy(ast.ymin),
            ymax=copy.deepcopy(ast.ymax),
            zmin=copy.deepcopy(ast.zmin),
            zmax=copy.deepcopy(ast.zmax),
        )
