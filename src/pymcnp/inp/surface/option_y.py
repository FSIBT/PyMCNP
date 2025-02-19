import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class SurfaceOption_Y(_option.SurfaceOption_, keyword='y'):
    """
    Represents INP surface card y options.

    Attributes:
        y1: Y-axisymmetric point-defined surface point #1 y component.
        r1: Y-axisymmetric point-defined surface point #1 radius.
        y2: Y-axisymmetric point-defined surface point #2 y component.
        r2: Y-axisymmetric point-defined surface point #2 radius.
        y3: Y-axisymmetric point-defined surface point #3 y component.
        r3: Y-axisymmetric point-defined surface point #3 radius.
    """

    _REGEX = re.compile(r'\Ay( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)\Z')

    def __init__(
        self,
        y1: types.Real,
        r1: types.Real,
        y2: types.Real,
        r2: types.Real,
        y3: types.Real,
        r3: types.Real,
    ):
        """
        Initializes ``SurfaceOption_Y``.

        Parameters:
            y1: Y-axisymmetric point-defined surface point #1 y component.
            r1: Y-axisymmetric point-defined surface point #1 radius.
            y2: Y-axisymmetric point-defined surface point #2 y component.
            r2: Y-axisymmetric point-defined surface point #2 radius.
            y3: Y-axisymmetric point-defined surface point #3 y component.
            r3: Y-axisymmetric point-defined surface point #3 radius.

        Returns:
            ``SurfaceOption_Y``.

        Raises:
            InpError: SYNTAX_OPTION_VALUE.
        """

        if y1 is None:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION_VALUE, y1)
        if r1 is None:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION_VALUE, r1)
        if y2 is None:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION_VALUE, y2)
        if r2 is None:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION_VALUE, r2)
        if y3 is None:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION_VALUE, y3)
        if r3 is None:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION_VALUE, r3)

        self.value: typing.Final[tuple[any]] = types._Tuple([y1, r1, y2, r2, y3, r3])
        self.y1: typing.Final[types.Real] = y1
        self.r1: typing.Final[types.Real] = r1
        self.y2: typing.Final[types.Real] = y2
        self.r2: typing.Final[types.Real] = r2
        self.y3: typing.Final[types.Real] = y3
        self.r3: typing.Final[types.Real] = r3

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SurfaceOption_Y`` from INP.

        Parameters:
            source: INP surface card option.

        Returns:
            ``SurfaceOption_Y``.

        Raises:
            InpError: SYNTAX_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SurfaceOption_Y._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        y1 = types.Real.from_mcnp(tokens[1])
        r1 = types.Real.from_mcnp(tokens[2])
        y2 = types.Real.from_mcnp(tokens[3])
        r2 = types.Real.from_mcnp(tokens[4])
        y3 = types.Real.from_mcnp(tokens[5])
        r3 = types.Real.from_mcnp(tokens[6])

        return SurfaceOption_Y(y1, r1, y2, r2, y3, r3)
