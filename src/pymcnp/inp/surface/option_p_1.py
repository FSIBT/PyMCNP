import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class SurfaceOption_P1(_option.SurfaceOption_, keyword='p'):
    """
    Represents INP surface card p_1 options.

    Attributes:
        x1: point-defined general plane x-coordinate #1.
        y1: point-defined general plane y-coordinate #1.
        z1: point-defined general plane z-coordinate #1.
        x2: point-defined general plane x-coordinate #2.
        y2: point-defined general plane y-coordinate #2.
        z2: point-defined general plane z-coordinate #2.
        x3: point-defined general plane x-coordinate #3.
        y3: point-defined general plane y-coordinate #3.
        z3: point-defined general plane z-coordinate #3.
    """

    _REGEX = re.compile(r'\Ap( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)\Z')

    def __init__(
        self,
        x1: types.Real,
        y1: types.Real,
        z1: types.Real,
        x2: types.Real,
        y2: types.Real,
        z2: types.Real,
        x3: types.Real,
        y3: types.Real,
        z3: types.Real,
    ):
        """
        Initializes ``SurfaceOption_P1``.

        Parameters:
            x1: point-defined general plane x-coordinate #1.
            y1: point-defined general plane y-coordinate #1.
            z1: point-defined general plane z-coordinate #1.
            x2: point-defined general plane x-coordinate #2.
            y2: point-defined general plane y-coordinate #2.
            z2: point-defined general plane z-coordinate #2.
            x3: point-defined general plane x-coordinate #3.
            y3: point-defined general plane y-coordinate #3.
            z3: point-defined general plane z-coordinate #3.

        Returns:
            ``SurfaceOption_P1``.

        Raises:
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
        """

        if x1 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, x1)
        if y1 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, y1)
        if z1 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, z1)
        if x2 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, x2)
        if y2 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, y2)
        if z2 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, z2)
        if x3 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, x3)
        if y3 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, y3)
        if z3 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, z3)

        self.value: typing.Final[tuple[any]] = types._Tuple([x1, y1, z1, x2, y2, z2, x3, y3, z3])
        self.x1: typing.Final[types.Real] = x1
        self.y1: typing.Final[types.Real] = y1
        self.z1: typing.Final[types.Real] = z1
        self.x2: typing.Final[types.Real] = x2
        self.y2: typing.Final[types.Real] = y2
        self.z2: typing.Final[types.Real] = z2
        self.x3: typing.Final[types.Real] = x3
        self.y3: typing.Final[types.Real] = y3
        self.z3: typing.Final[types.Real] = z3

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SurfaceOption_P1`` from INP.

        Parameters:
            source: INP surface card option.

        Returns:
            ``SurfaceOption_P1``.

        Raises:
            McnpError: SYNTAX_SURFACE_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SurfaceOption_P1._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_SURFACE_OPTION, source)

        x1 = types.Real.from_mcnp(tokens[1])
        y1 = types.Real.from_mcnp(tokens[2])
        z1 = types.Real.from_mcnp(tokens[3])
        x2 = types.Real.from_mcnp(tokens[4])
        y2 = types.Real.from_mcnp(tokens[5])
        z2 = types.Real.from_mcnp(tokens[6])
        x3 = types.Real.from_mcnp(tokens[7])
        y3 = types.Real.from_mcnp(tokens[8])
        z3 = types.Real.from_mcnp(tokens[9])

        return SurfaceOption_P1(x1, y1, z1, x2, y2, z2, x3, y3, z3)
