import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser
from ...utils import _visualization


class SurfaceOption_Sph(_option.SurfaceOption_, keyword='sph'):
    """
    Represents INP surface card sph options.

    Attributes:
        vx: Sphere macrobody position vector x component.
        vy: Sphere macrobody position vector y component.
        vz: Sphere macrobody position vector z component.
        r: Sphere macrobody radius.
    """

    _REGEX = re.compile(r'\Asph( \S+)( \S+)( \S+)( \S+)\Z')

    def __init__(self, vx: types.Real, vy: types.Real, vz: types.Real, r: types.Real):
        """
        Initializes ``SurfaceOption_Sph``.

        Parameters:
            vx: Sphere macrobody position vector x component.
            vy: Sphere macrobody position vector y component.
            vz: Sphere macrobody position vector z component.
            r: Sphere macrobody radius.

        Returns:
            ``SurfaceOption_Sph``.

        Raises:
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
        """

        if vx is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, vx)
        if vy is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, vy)
        if vz is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, vz)
        if r is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, r)

        self.value: typing.Final[tuple[any]] = types._Tuple([vx, vy, vz, r])
        self.vx: typing.Final[types.Real] = vx
        self.vy: typing.Final[types.Real] = vy
        self.vz: typing.Final[types.Real] = vz
        self.r: typing.Final[types.Real] = r

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SurfaceOption_Sph`` from INP.

        Parameters:
            source: INP surface card option.

        Returns:
            ``SurfaceOption_Sph``.

        Raises:
            McnpError: SYNTAX_SURFACE_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SurfaceOption_Sph._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_SURFACE_OPTION, source)

        vx = types.Real.from_mcnp(tokens[1])
        vy = types.Real.from_mcnp(tokens[2])
        vz = types.Real.from_mcnp(tokens[3])
        r = types.Real.from_mcnp(tokens[4])

        return SurfaceOption_Sph(vx, vy, vz, r)

    def to_pyvista(self):
        """
        Generates ``pyvista.PolyData`` from ``SurfaceOption_Sph``.

        Returns:
            ``pyvista.PolyData`` for ``SurfaceOption_Sph``
        """

        vis = _visualization.McnpVisualization.get_sphere(self.r.value)
        vis = vis.add_translation(
            _visualization.Vector(self.vx.value, self.vy.value, self.vz.value)
        )

        return vis.data
