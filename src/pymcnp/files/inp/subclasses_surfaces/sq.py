"""
Contains the ``Sq`` subclass of ``Surface``."""

from typing import Final

from ..surface import Surface, SurfaceMnemonic
from ....utils import types, errors, _parser


class Sq(Surface):
    """
    Represents INP sq surface cards.

    ``Sq`` implements ``Surface``.

    Attributes:
        a: Oblique special quadratic A coefficent.
        b: Oblique special quadratic B coefficent.
        c: Oblique special quadratic C coefficent.
        d: Oblique special quadratic D coefficent.
        e: Oblique special quadratic E coefficent.
        f: Oblique special quadratic F coefficent.
        g: Oblique special quadratic G coefficent.
        x: Oblique special quadratic center x component.
        y: Oblique special quadratic center y component.
        z: Oblique special quadratic center z component.
    """

    def __init__(
        self,
        number: types.McnpInteger,
        transform: types.McnpInteger,
        a: types.McnpReal,
        b: types.McnpReal,
        c: types.McnpReal,
        d: types.McnpReal,
        e: types.McnpReal,
        f: types.McnpReal,
        g: types.McnpReal,
        x: types.McnpReal,
        y: types.McnpReal,
        z: types.McnpReal,
        is_whiteboundary: bool = False,
        is_reflecting: bool = False,
    ):
        """
        Initializes ``Sq``.


        Parameters:
            a: Oblique special quadratic A coefficent.
            b: Oblique special quadratic B coefficent.
            c: Oblique special quadratic C coefficent.
            d: Oblique special quadratic D coefficent.
            e: Oblique special quadratic E coefficent.
            f: Oblique special quadratic F coefficent.
            g: Oblique special quadratic G coefficent.
            x: Oblique special quadratic center x component.
            y: Oblique special quadratic center y component.
            z: Oblique special quadratic center z component.

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

        if e is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(e))

        if f is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(f))

        if g is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(g))

        if x is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(x))

        if y is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(y))

        if z is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(z))

        self.ident: Final[int] = number.value
        self.number: Final[types.McnpInteger] = number
        self.mnemonic: Final[SurfaceMnemonic] = SurfaceMnemonic.SQ
        self.transform: Final[types.McnpInteger] = transform
        self.is_reflecting: Final[bool] = is_reflecting
        self.is_whiteboundary: Final[bool] = is_whiteboundary

        self.a: Final[types.McnpReal] = a
        self.b: Final[types.McnpReal] = b
        self.c: Final[types.McnpReal] = c
        self.d: Final[types.McnpReal] = d
        self.e: Final[types.McnpReal] = e
        self.f: Final[types.McnpReal] = f
        self.g: Final[types.McnpReal] = g
        self.x: Final[types.McnpReal] = x
        self.y: Final[types.McnpReal] = y
        self.z: Final[types.McnpReal] = z
        self.parameters: Final[tuple[types.McnpReal]] = tuple([a, b, c, d, e, f, g, x, y, z])

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Sq`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for surface.

        Returns:
            ``Sq`` object.

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

        a = types.McnpReal.from_mcnp(tokens.popl())
        b = types.McnpReal.from_mcnp(tokens.popl())
        c = types.McnpReal.from_mcnp(tokens.popl())
        d = types.McnpReal.from_mcnp(tokens.popl())
        e = types.McnpReal.from_mcnp(tokens.popl())
        f = types.McnpReal.from_mcnp(tokens.popl())
        g = types.McnpReal.from_mcnp(tokens.popl())
        x = types.McnpReal.from_mcnp(tokens.popl())
        y = types.McnpReal.from_mcnp(tokens.popl())
        z = types.McnpReal.from_mcnp(tokens.popl())

        return Sq(
            number,
            transform,
            mnemonic,
            a,
            b,
            c,
            d,
            e,
            f,
            g,
            x,
            y,
            z,
            is_whiteboundary=is_whiteboundary,
            is_reflecting=is_reflecting,
        )
