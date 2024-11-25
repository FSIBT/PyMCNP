"""
Contains the ``Sz`` subclass of ``Surface``.
"""

from typing import Final

from ..surface import Surface, SurfaceMnemonic
from ...utils import types, errors, _parser


class Sz(Surface):
    """
    Represents INP sz surface cards.

    ``Sz`` implements ``Surface``.

    Attributes:
        z: On-z-axis sphere center z component.
        r: On-z-axis sphere radius.
    """

    def __init__(
        self,
        number: types.McnpInteger,
        transform: types.McnpInteger,
        z: types.McnpReal,
        r: types.McnpReal,
        is_whiteboundary: bool = False,
        is_reflecting: bool = False,
    ):
        """
        Initializes ``Sz``.


        Parameters:
            z: On-z-axis sphere center z component.
            r: On-z-axis sphere radius.

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

        if z is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(z))

        if r is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(r))

        self.ident: Final[int] = number.value
        self.number: Final[types.McnpInteger] = number
        self.mnemonic: Final[SurfaceMnemonic] = SurfaceMnemonic.SZ
        self.transform: Final[types.McnpInteger] = transform
        self.is_reflecting: Final[bool] = is_reflecting
        self.is_whiteboundary: Final[bool] = is_whiteboundary

        self.z: Final[types.McnpReal] = z
        self.r: Final[types.McnpReal] = r
        self.parameters: Final[tuple[types.McnpReal]] = tuple([z, r])

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Sz`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for surface.

        Returns:
            ``Sz`` object.

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

        if tokens.popl() != 'sz':
            raise errors.McnpError(errors.McnpCode.UNRECOGNIZED_KEYWORD, info=source)

        z = types.McnpReal.from_mcnp(tokens.popl())
        r = types.McnpReal.from_mcnp(tokens.popl())

        return Sz(
            number, transform, z, r, is_whiteboundary=is_whiteboundary, is_reflecting=is_reflecting
        )
