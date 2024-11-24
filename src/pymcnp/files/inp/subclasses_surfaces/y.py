"""
Contains the ``Y`` subclass of ``Surface``."""

from typing import Final

from ..surface import Surface, SurfaceMnemonic
from ....utils import types, errors, _parser


class Y(Surface):
    """
    Represents INP y surface cards.

    ``Y`` implements ``Surface``.

    Attributes:
        y1: Y-axisymmetric point-defined surface point #1 y component.
        r1: Y-axisymmetric point-defined surface point #1 radius.
        y2: Y-axisymmetric point-defined surface point #2 y component.
        r2: Y-axisymmetric point-defined surface point #2 radius.
        y3: Y-axisymmetric point-defined surface point #3 y component.
        r3: Y-axisymmetric point-defined surface point #3 radius.
    """

    def __init__(
        self,
        number: types.McnpInteger,
        transform: types.McnpInteger,
        y1: types.McnpReal,
        r1: types.McnpReal,
        y2: types.McnpReal,
        r2: types.McnpReal,
        y3: types.McnpReal,
        r3: types.McnpReal,
        is_whiteboundary: bool = False,
        is_reflecting: bool = False,
    ):
        """
        Initializes ``Y``.


        Parameters:
            y1: Y-axisymmetric point-defined surface point #1 y component.
            r1: Y-axisymmetric point-defined surface point #1 radius.
            y2: Y-axisymmetric point-defined surface point #2 y component.
            r2: Y-axisymmetric point-defined surface point #2 radius.
            y3: Y-axisymmetric point-defined surface point #3 y component.
            r3: Y-axisymmetric point-defined surface point #3 radius.

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

        if y1 is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(y1))

        if r1 is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(r1))

        if y2 is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(y2))

        if r2 is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(r2))

        if y3 is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(y3))

        if r3 is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(r3))

        self.ident: Final[int] = number.value
        self.number: Final[types.McnpInteger] = number
        self.mnemonic: Final[SurfaceMnemonic] = SurfaceMnemonic.Y
        self.transform: Final[types.McnpInteger] = transform
        self.is_reflecting: Final[bool] = is_reflecting
        self.is_whiteboundary: Final[bool] = is_whiteboundary

        self.y1: Final[types.McnpReal] = y1
        self.r1: Final[types.McnpReal] = r1
        self.y2: Final[types.McnpReal] = y2
        self.r2: Final[types.McnpReal] = r2
        self.y3: Final[types.McnpReal] = y3
        self.r3: Final[types.McnpReal] = r3
        self.parameters: Final[tuple[types.McnpReal]] = tuple([y1, r1, y2, r2, y3, r3])

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Y`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for surface.

        Returns:
            ``Y`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
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

        mnemonic = SurfaceMnemonic.from_mcnp(tokens.popl())

        y1 = types.McnpReal.from_mcnp(tokens.popl())
        r1 = types.McnpReal.from_mcnp(tokens.popl())
        y2 = types.McnpReal.from_mcnp(tokens.popl())
        r2 = types.McnpReal.from_mcnp(tokens.popl())
        y3 = types.McnpReal.from_mcnp(tokens.popl())
        r3 = types.McnpReal.from_mcnp(tokens.popl())

        return Y(
            number,
            transform,
            mnemonic,
            y1,
            r1,
            y2,
            r2,
            y3,
            r3,
            is_whiteboundary=is_whiteboundary,
            is_reflecting=is_reflecting,
        )
