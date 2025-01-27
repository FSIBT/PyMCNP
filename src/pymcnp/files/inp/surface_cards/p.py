"""
Contains the ``P`` subclass of ``Surface``.
"""

from typing import Final

from ..surface import Surface
from ..surface_mnemonic import SurfaceMnemonic
from ...utils import types
from ...utils import errors
from ...utils import _parser


class P(Surface):
    """
    Represents INP p surface cards.

    ``P`` implements ``Surface``.

    Attributes:
        a: Equation-defined general plane A coefficent.
        b: Equation-defined general plane B coefficent.
        c: Equation-defined general plane C coefficent.
        d: Equation-defined general plane D coefficent.
    """

    def __init__(
        self,
        number: types.McnpInteger,
        transform: types.McnpInteger,
        a: types.McnpReal,
        b: types.McnpReal,
        c: types.McnpReal,
        d: types.McnpReal,
        is_whiteboundary: bool = False,
        is_reflecting: bool = False,
    ):
        """
        Initializes ``P``.


        Parameters:
            a: Equation-defined general plane A coefficent.
            b: Equation-defined general plane B coefficent.
            c: Equation-defined general plane C coefficent.
            d: Equation-defined general plane D coefficent.

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

        if a is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(a))

        if b is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(b))

        if c is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(c))

        if d is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(d))

        self.ident: Final[int] = number.value
        self.number: Final[types.McnpInteger] = number
        self.mnemonic: Final[SurfaceMnemonic] = SurfaceMnemonic.P
        self.transform: Final[types.McnpInteger] = transform
        self.is_reflecting: Final[bool] = is_reflecting
        self.is_whiteboundary: Final[bool] = is_whiteboundary

        self.a: Final[types.McnpReal] = a
        self.b: Final[types.McnpReal] = b
        self.c: Final[types.McnpReal] = c
        self.d: Final[types.McnpReal] = d
        self.parameters: Final[tuple[types.McnpReal]] = tuple([a, b, c, d])

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``P`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for surface.

        Returns:
            ``P`` object.

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

        if tokens.popl() != 'p':
            raise errors.McnpError(errors.McnpCode.UNRECOGNIZED_KEYWORD, info=source)

        a = types.McnpReal.from_mcnp(tokens.popl())
        b = types.McnpReal.from_mcnp(tokens.popl())
        c = types.McnpReal.from_mcnp(tokens.popl())
        d = types.McnpReal.from_mcnp(tokens.popl())

        return P(
            number,
            transform,
            a,
            b,
            c,
            d,
            is_whiteboundary=is_whiteboundary,
            is_reflecting=is_reflecting,
        )
