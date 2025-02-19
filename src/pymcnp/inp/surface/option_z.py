import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class SurfaceOption_Z(_option.SurfaceOption_, keyword='z'):
    """
    Represents INP surface card z options.

    Attributes:
        z1: Z-axisymmetric point-defined surface point #1 z component.
        r1: Z-axisymmetric point-defined surface point #1 radius.
        z2: Z-axisymmetric point-defined surface point #2 z component.
        r2: Z-axisymmetric point-defined surface point #2 radius.
        z3: Z-axisymmetric point-defined surface point #3 z component.
        r3: Z-axisymmetric point-defined surface point #3 radius.
    """

    _REGEX = re.compile(r'\Az( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)\Z')

    def __init__(
        self,
        z1: types.Real,
        r1: types.Real,
        z2: types.Real,
        r2: types.Real,
        z3: types.Real,
        r3: types.Real,
    ):
        """
        Initializes ``SurfaceOption_Z``.

        Parameters:
            z1: Z-axisymmetric point-defined surface point #1 z component.
            r1: Z-axisymmetric point-defined surface point #1 radius.
            z2: Z-axisymmetric point-defined surface point #2 z component.
            r2: Z-axisymmetric point-defined surface point #2 radius.
            z3: Z-axisymmetric point-defined surface point #3 z component.
            r3: Z-axisymmetric point-defined surface point #3 radius.

        Returns:
            ``SurfaceOption_Z``.

        Raises:
            InpError: SYNTAX_OPTION_VALUE.
        """

        if z1 is None:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION_VALUE, z1)
        if r1 is None:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION_VALUE, r1)
        if z2 is None:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION_VALUE, z2)
        if r2 is None:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION_VALUE, r2)
        if z3 is None:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION_VALUE, z3)
        if r3 is None:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION_VALUE, r3)

        self.value: typing.Final[tuple[any]] = types._Tuple([z1, r1, z2, r2, z3, r3])
        self.z1: typing.Final[types.Real] = z1
        self.r1: typing.Final[types.Real] = r1
        self.z2: typing.Final[types.Real] = z2
        self.r2: typing.Final[types.Real] = r2
        self.z3: typing.Final[types.Real] = z3
        self.r3: typing.Final[types.Real] = r3

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SurfaceOption_Z`` from INP.

        Parameters:
            source: INP surface card option.

        Returns:
            ``SurfaceOption_Z``.

        Raises:
            InpError: SYNTAX_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SurfaceOption_Z._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        z1 = types.Real.from_mcnp(tokens[1])
        r1 = types.Real.from_mcnp(tokens[2])
        z2 = types.Real.from_mcnp(tokens[3])
        r2 = types.Real.from_mcnp(tokens[4])
        z3 = types.Real.from_mcnp(tokens[5])
        r3 = types.Real.from_mcnp(tokens[6])

        return SurfaceOption_Z(z1, r1, z2, r2, z3, r3)
