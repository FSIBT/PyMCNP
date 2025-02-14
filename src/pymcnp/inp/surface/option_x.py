import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class SurfaceOption_X(_option.SurfaceOption_, keyword='x'):
    """
    Represents INP surface card x options.

    Attributes:
        x1: X-axisymmetric point-defined surface point #1 x component.
        r1: X-axisymmetric point-defined surface point #1 radius.
        x2: X-axisymmetric point-defined surface point #2 x component.
        r2: X-axisymmetric point-defined surface point #2 radius.
        x3: X-axisymmetric point-defined surface point #3 x component.
        r3: X-axisymmetric point-defined surface point #3 radius.
    """

    _REGEX = re.compile(r'\Ax( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)\Z')

    def __init__(
        self,
        x1: types.Real,
        r1: types.Real,
        x2: types.Real,
        r2: types.Real,
        x3: types.Real,
        r3: types.Real,
    ):
        """
        Initializes ``SurfaceOption_X``.

        Parameters:
            x1: X-axisymmetric point-defined surface point #1 x component.
            r1: X-axisymmetric point-defined surface point #1 radius.
            x2: X-axisymmetric point-defined surface point #2 x component.
            r2: X-axisymmetric point-defined surface point #2 radius.
            x3: X-axisymmetric point-defined surface point #3 x component.
            r3: X-axisymmetric point-defined surface point #3 radius.

        Returns:
            ``SurfaceOption_X``.

        Raises:
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
        """

        if x1 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, x1)
        if r1 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, r1)
        if x2 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, x2)
        if r2 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, r2)
        if x3 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, x3)
        if r3 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, r3)

        self.value: typing.Final[tuple[any]] = types._Tuple([x1, r1, x2, r2, x3, r3])
        self.x1: typing.Final[types.Real] = x1
        self.r1: typing.Final[types.Real] = r1
        self.x2: typing.Final[types.Real] = x2
        self.r2: typing.Final[types.Real] = r2
        self.x3: typing.Final[types.Real] = x3
        self.r3: typing.Final[types.Real] = r3

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SurfaceOption_X`` from INP.

        Parameters:
            source: INP surface card option.

        Returns:
            ``SurfaceOption_X``.

        Raises:
            McnpError: SYNTAX_SURFACE_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SurfaceOption_X._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_SURFACE_OPTION, source)

        x1 = types.Real.from_mcnp(tokens[1])
        r1 = types.Real.from_mcnp(tokens[2])
        x2 = types.Real.from_mcnp(tokens[3])
        r2 = types.Real.from_mcnp(tokens[4])
        x3 = types.Real.from_mcnp(tokens[5])
        r3 = types.Real.from_mcnp(tokens[6])

        return SurfaceOption_X(x1, r1, x2, r2, x3, r3)
