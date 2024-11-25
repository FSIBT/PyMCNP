"""
Contains the ``X`` subclass of ``Surface``.
"""

from typing import Final

from ..surface import Surface, SurfaceMnemonic
from ...utils import types, errors, _parser


class X(Surface):
    """
    Represents INP x surface cards.

    ``X`` implements ``Surface``.

    Attributes:
        x1: X-axisymmetric point-defined surface point #1 x component.
        r1: X-axisymmetric point-defined surface point #1 radius.
        x2: X-axisymmetric point-defined surface point #2 x component.
        r2: X-axisymmetric point-defined surface point #2 radius.
        x3: X-axisymmetric point-defined surface point #3 x component.
        r3: X-axisymmetric point-defined surface point #3 radius.
    """

    def __init__(
        self,
        number: types.McnpInteger,
        transform: types.McnpInteger,
        x1: types.McnpReal,
        r1: types.McnpReal,
        x2: types.McnpReal,
        r2: types.McnpReal,
        x3: types.McnpReal,
        r3: types.McnpReal,
        is_whiteboundary: bool = False,
        is_reflecting: bool = False,
    ):
        """
        Initializes ``X``.


        Parameters:
            x1: X-axisymmetric point-defined surface point #1 x component.
            r1: X-axisymmetric point-defined surface point #1 radius.
            x2: X-axisymmetric point-defined surface point #2 x component.
            r2: X-axisymmetric point-defined surface point #2 radius.
            x3: X-axisymmetric point-defined surface point #3 x component.
            r3: X-axisymmetric point-defined surface point #3 radius.

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

        if x1 is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(x1))

        if r1 is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(r1))

        if x2 is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(x2))

        if r2 is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(r2))

        if x3 is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(x3))

        if r3 is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(r3))

        self.ident: Final[int] = number.value
        self.number: Final[types.McnpInteger] = number
        self.mnemonic: Final[SurfaceMnemonic] = SurfaceMnemonic.X
        self.transform: Final[types.McnpInteger] = transform
        self.is_reflecting: Final[bool] = is_reflecting
        self.is_whiteboundary: Final[bool] = is_whiteboundary

        self.x1: Final[types.McnpReal] = x1
        self.r1: Final[types.McnpReal] = r1
        self.x2: Final[types.McnpReal] = x2
        self.r2: Final[types.McnpReal] = r2
        self.x3: Final[types.McnpReal] = x3
        self.r3: Final[types.McnpReal] = r3
        self.parameters: Final[tuple[types.McnpReal]] = tuple([x1, r1, x2, r2, x3, r3])

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``X`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for surface.

        Returns:
            ``X`` object.

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

        if tokens.popl() != 'x':
            raise errors.McnpError(errors.McnpCode.UNRECOGNIZED_KEYWORD, info=source)

        x1 = types.McnpReal.from_mcnp(tokens.popl())
        r1 = types.McnpReal.from_mcnp(tokens.popl())
        x2 = types.McnpReal.from_mcnp(tokens.popl())
        r2 = types.McnpReal.from_mcnp(tokens.popl())
        x3 = types.McnpReal.from_mcnp(tokens.popl())
        r3 = types.McnpReal.from_mcnp(tokens.popl())

        return X(
            number,
            transform,
            x1,
            r1,
            x2,
            r2,
            x3,
            r3,
            is_whiteboundary=is_whiteboundary,
            is_reflecting=is_reflecting,
        )
