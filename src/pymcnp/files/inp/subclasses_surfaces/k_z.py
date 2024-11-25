"""
Contains the ``K_z`` subclass of ``Surface``.
"""

from typing import Final

from ..surface import Surface, SurfaceMnemonic
from ...utils import types, errors, _parser


class K_z(Surface):
    """
    Represents INP k/z surface cards.

    ``K_z`` implements ``Surface``.

    Attributes:
        x: Parallel-to-z-axis cone center x component.
        y: Parallel-to-z-axis cone center y component.
        z: Parallel-to-z-axis cone center z component.
        t_squared: Parallel-to-z-axis cone t^2 coefficent.
        plusminus_1: Parallel-to-z-axis cone sheet selector.
    """

    def __init__(
        self,
        number: types.McnpInteger,
        transform: types.McnpInteger,
        x: types.McnpReal,
        y: types.McnpReal,
        z: types.McnpReal,
        t_squared: types.McnpReal,
        plusminus_1: types.McnpReal,
        is_whiteboundary: bool = False,
        is_reflecting: bool = False,
    ):
        """
        Initializes ``K_z``.


        Parameters:
            x: Parallel-to-z-axis cone center x component.
            y: Parallel-to-z-axis cone center y component.
            z: Parallel-to-z-axis cone center z component.
            t_squared: Parallel-to-z-axis cone t^2 coefficent.
            plusminus_1: Parallel-to-z-axis cone sheet selector.

        Raises:
            McnpError: INVALID_SURFACE_NUMBER.
            McnpError: INVALID_SURFACE_TRANSFORMPERIODIC.
            McnpError: INVALID_SURFACE_WHITEBOUNDARY.
            McnpError: INVALID_SURFACE_REFLECTING.
            McnpError: INVALID_SURFACE_PARAMETER.
        """

        if number is None or not (1 <= number <= 99_999_999):
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_NUMBER, str(number))

        if transform is not None and not (-99_999_999 <= transform <= 999):
            raise errors.McnpError(
                errors.McnpCode.INVALID_SURFACE_TRANSFORMPERIODIC, str(transform)
            )

        if is_whiteboundary is None:
            raise errors.McnpError(
                errors.McnpCode.INVALID_SURFACE_WHITEBOUNDARY, str(is_whiteboundary)
            )

        if is_reflecting is None or (is_reflecting and is_whiteboundary):
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_REFLECTING, str(is_reflecting))

        if x is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(x))

        if y is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(y))

        if z is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(z))

        if t_squared is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(t_squared))

        if plusminus_1 is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(plusminus_1))

        self.ident: Final[int] = number.value
        self.number: Final[types.McnpInteger] = number
        self.mnemonic: Final[SurfaceMnemonic] = SurfaceMnemonic.K_Z
        self.transform: Final[types.McnpInteger] = transform
        self.is_reflecting: Final[bool] = is_reflecting
        self.is_whiteboundary: Final[bool] = is_whiteboundary

        self.x: Final[types.McnpReal] = x
        self.y: Final[types.McnpReal] = y
        self.z: Final[types.McnpReal] = z
        self.t_squared: Final[types.McnpReal] = t_squared
        self.plusminus_1: Final[types.McnpReal] = plusminus_1
        self.parameters: Final[tuple[types.McnpReal]] = tuple([x, y, z, t_squared, plusminus_1])

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``K_z`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for surface.

        Returns:
            ``K_z`` object.

        Raises:
            McnpError: EXPECTED_TOKEN.
            McnpError: UNEXPECTED_TOKEN.
            McnpError: UNRECOGNIZED_KEYWORD.
        """

        source = _parser.Preprocessor.process_inp(source)
        source, comments = _parser.Preprocessor.process_inp_comments(source)
        tokens = _parser.Parser(
            source.split(' '),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.peekl()[0] == '+':
            is_whiteboundary = True
            is_reflecting = False
            tokens.pushl(tokens.popl()[1:])
        elif tokens.peekl()[0] == '*':
            is_whiteboundary = False
            is_reflecting = True
            tokens.pushl(tokens.popl()[1:])
        else:
            is_whiteboundary = False
            is_reflecting = False

        number = types.McnpInteger.from_mcnp(tokens.popl())

        try:
            transform = types.McnpInteger.from_mcnp(tokens.peekl())
            tokens.popl()
        except Exception:
            transform = None

        if tokens.popl() != 'k/z':
            raise errors.McnpError(errors.McnpCode.UNRECOGNIZED_KEYWORD, info=source)

        x = types.McnpReal.from_mcnp(tokens.popl())
        y = types.McnpReal.from_mcnp(tokens.popl())
        z = types.McnpReal.from_mcnp(tokens.popl())
        t_squared = types.McnpReal.from_mcnp(tokens.popl())
        plusminus_1 = types.McnpReal.from_mcnp(tokens.popl())

        return K_z(
            number,
            transform,
            x,
            y,
            z,
            t_squared,
            plusminus_1,
            is_whiteboundary=is_whiteboundary,
            is_reflecting=is_reflecting,
        )
