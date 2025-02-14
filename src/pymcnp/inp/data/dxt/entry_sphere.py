import re
import typing

from . import _entry
from ....utils import types
from ....utils import errors
from ....utils import _parser


class DxtEntry_Sphere(_entry.DxtEntry_):
    """
    Represents INP data card data option sphere entries.

    Attributes:
        x: Vector x coordinate.
        y: Vector y coordinate.
        z: Vector z coordinate.
        inner_radius: Inner sphere radius.
        outer_radius: Outer sphere radius.
    """

    _REGEX = re.compile(r'( \S+)( \S+)( \S+)( \S+)( \S+)')

    def __init__(
        self,
        x: types.Real,
        y: types.Real,
        z: types.Real,
        inner_radius: types.Integer,
        outer_radius: types.Integer,
    ):
        """
        Initializes ``DxtEntry_Sphere``.

        Parameters:
            x: Vector x coordinate.
            y: Vector y coordinate.
            z: Vector z coordinate.
            inner_radius: Inner sphere radius.
            outer_radius: Outer sphere radius.

        Returns:
            ``DxtEntrySphere``.

        Raises:
            McnpError: SEMANTICS_DATA_ENTRY_VALUE.
        """

        if x is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_ENTRY_VALUE, x)
        if y is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_ENTRY_VALUE, y)
        if z is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_ENTRY_VALUE, z)
        if inner_radius is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_ENTRY_VALUE, inner_radius)
        if outer_radius is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_ENTRY_VALUE, outer_radius)

        self.parameters: typing.Final[tuple[any]] = types._Tuple(
            [x, y, z, inner_radius, outer_radius]
        )
        self.x: typing.Final[types.Real] = x
        self.y: typing.Final[types.Real] = y
        self.z: typing.Final[types.Real] = z
        self.inner_radius: typing.Final[types.Integer] = inner_radius
        self.outer_radius: typing.Final[types.Integer] = outer_radius

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DxtEntry_Sphere`` from INP.

        Parameters:
            INP for ``DxtEntry_Sphere``.

        Returns:
            ``DxtEntry_Sphere``.

        Raises:
            McnpError: SYNTAX_DXT_ENTRY.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DxtEntry_Sphere._REGEX.match(' ' + source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_DXT_ENTRY, source)

        x = types.Real.from_mcnp(tokens[1])
        y = types.Real.from_mcnp(tokens[2])
        z = types.Real.from_mcnp(tokens[3])
        inner_radius = types.Integer.from_mcnp(tokens[4])
        outer_radius = types.Integer.from_mcnp(tokens[5])

        return DxtEntry_Sphere(x, y, z, inner_radius, outer_radius)
