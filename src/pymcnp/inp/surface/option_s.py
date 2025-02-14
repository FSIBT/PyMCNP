import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser
from ...utils import _visualization


class SurfaceOption_S(_option.SurfaceOption_, keyword='s'):
    """
    Represents INP surface card s options.

    Attributes:
        x: General sphere center x component.
        y: General sphere center y component.
        z: General sphere center z component.
        r: General sphere radius.
    """

    _REGEX = re.compile(r'\As( \S+)( \S+)( \S+)( \S+)\Z')

    def __init__(self, x: types.Real, y: types.Real, z: types.Real, r: types.Real):
        """
        Initializes ``SurfaceOption_S``.

        Parameters:
            x: General sphere center x component.
            y: General sphere center y component.
            z: General sphere center z component.
            r: General sphere radius.

        Returns:
            ``SurfaceOption_S``.

        Raises:
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
        """

        if x is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, x)
        if y is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, y)
        if z is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, z)
        if r is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, r)

        self.value: typing.Final[tuple[any]] = types._Tuple([x, y, z, r])
        self.x: typing.Final[types.Real] = x
        self.y: typing.Final[types.Real] = y
        self.z: typing.Final[types.Real] = z
        self.r: typing.Final[types.Real] = r

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SurfaceOption_S`` from INP.

        Parameters:
            source: INP surface card option.

        Returns:
            ``SurfaceOption_S``.

        Raises:
            McnpError: SYNTAX_SURFACE_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SurfaceOption_S._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_SURFACE_OPTION, source)

        x = types.Real.from_mcnp(tokens[1])
        y = types.Real.from_mcnp(tokens[2])
        z = types.Real.from_mcnp(tokens[3])
        r = types.Real.from_mcnp(tokens[4])

        return SurfaceOption_S(x, y, z, r)

    def to_pyvista(self):
        """
        Generates ``pyvista[.]PolyData`` from ``SurfaceOption_S``.

        Returns:
            ``pyvista[.]PolyData`` for ``SurfaceOption_S``
        """

        vis = _visualization.PyMcnpVisualization.get_sphere(self.r.value)
        vis = vis.add_translation(_visualization.Vector(self.x.value, self.y.value, self.z.value))

        return vis.data
