import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser
from ...utils import _visualization


class SurfaceOption_Sz(_option.SurfaceOption_, keyword='sz'):
    """
    Represents INP surface card sz options.

    Attributes:
        z: On-z-axis sphere center z component.
        r: On-z-axis sphere radius.
    """

    _REGEX = re.compile(r'\Asz( \S+)( \S+)\Z')

    def __init__(self, z: types.Real, r: types.Real):
        """
        Initializes ``SurfaceOption_Sz``.

        Parameters:
            z: On-z-axis sphere center z component.
            r: On-z-axis sphere radius.

        Returns:
            ``SurfaceOption_Sz``.

        Raises:
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
        """

        if z is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, z)
        if r is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, r)

        self.value: typing.Final[tuple[any]] = types._Tuple([z, r])
        self.z: typing.Final[types.Real] = z
        self.r: typing.Final[types.Real] = r

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SurfaceOption_Sz`` from INP.

        Parameters:
            source: INP surface card option.

        Returns:
            ``SurfaceOption_Sz``.

        Raises:
            McnpError: SYNTAX_SURFACE_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SurfaceOption_Sz._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_SURFACE_OPTION, source)

        z = types.Real.from_mcnp(tokens[1])
        r = types.Real.from_mcnp(tokens[2])

        return SurfaceOption_Sz(z, r)

    def to_pyvista(self):
        """
        Generates ``pyvista[.]PolyData`` from ``SurfaceOption_Sz``.

        Returns:
            ``pyvista[.]PolyData`` for ``SurfaceOption_Sz``
        """

        vis = _visualization.PyMcnpVisualization.get_sphere(self.r.value)
        vis = vis.add_translation(_visualization.Vector(0, 0, self.z.value))

        return vis.data
