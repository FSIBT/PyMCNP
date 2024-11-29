"""
Contains the ``Box`` subclass of ``Surface``.
"""

from typing import Final

from ..surface import Surface
from ..surface_mnemonic import SurfaceMnemonic
from ...utils import types, errors, _parser


class Box(Surface):
    """
    Represents INP box surface cards.

    ``Box`` implements ``Surface``.

    Attributes:
        vx: Box macrobody position vector x component.
        vy: Box macrobody position vector y component.
        vz: Box macrobody position vector z component.
        a1x: Box macrobody vector #1 x component.
        a1y: Box macrobody vector #1 y component.
        a1z: Box macrobody vector #1 z component.
        a2x: Box macrobody vector #2 x component.
        a2y: Box macrobody vector #2 y component.
        a2z: Box macrobody vector #2 z component.
        a3x: Box macrobody vector #3 x component.
        a3y: Box macrobody vector #3 y component.
        a3z: Box macrobody vector #3 z component.
    """

    def __init__(
        self,
        number: types.McnpInteger,
        transform: types.McnpInteger,
        vx: types.McnpReal,
        vy: types.McnpReal,
        vz: types.McnpReal,
        a1x: types.McnpReal,
        a1y: types.McnpReal,
        a1z: types.McnpReal,
        a2x: types.McnpReal,
        a2y: types.McnpReal,
        a2z: types.McnpReal,
        a3x: types.McnpReal,
        a3y: types.McnpReal,
        a3z: types.McnpReal,
        is_whiteboundary: bool = False,
        is_reflecting: bool = False,
    ):
        """
        Initializes ``Box``.


        Parameters:
            vx: Box macrobody position vector x component.
            vy: Box macrobody position vector y component.
            vz: Box macrobody position vector z component.
            a1x: Box macrobody vector #1 x component.
            a1y: Box macrobody vector #1 y component.
            a1z: Box macrobody vector #1 z component.
            a2x: Box macrobody vector #2 x component.
            a2y: Box macrobody vector #2 y component.
            a2z: Box macrobody vector #2 z component.
            a3x: Box macrobody vector #3 x component.
            a3y: Box macrobody vector #3 y component.
            a3z: Box macrobody vector #3 z component.

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

        if vx is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(vx))

        if vy is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(vy))

        if vz is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(vz))

        if a1x is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(a1x))

        if a1y is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(a1y))

        if a1z is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(a1z))

        if a2x is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(a2x))

        if a2y is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(a2y))

        if a2z is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(a2z))

        if a3x is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(a3x))

        if a3y is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(a3y))

        if a3z is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(a3z))

        self.ident: Final[int] = number.value
        self.number: Final[types.McnpInteger] = number
        self.mnemonic: Final[SurfaceMnemonic] = SurfaceMnemonic.BOX
        self.transform: Final[types.McnpInteger] = transform
        self.is_reflecting: Final[bool] = is_reflecting
        self.is_whiteboundary: Final[bool] = is_whiteboundary

        self.vx: Final[types.McnpReal] = vx
        self.vy: Final[types.McnpReal] = vy
        self.vz: Final[types.McnpReal] = vz
        self.a1x: Final[types.McnpReal] = a1x
        self.a1y: Final[types.McnpReal] = a1y
        self.a1z: Final[types.McnpReal] = a1z
        self.a2x: Final[types.McnpReal] = a2x
        self.a2y: Final[types.McnpReal] = a2y
        self.a2z: Final[types.McnpReal] = a2z
        self.a3x: Final[types.McnpReal] = a3x
        self.a3y: Final[types.McnpReal] = a3y
        self.a3z: Final[types.McnpReal] = a3z
        self.parameters: Final[tuple[types.McnpReal]] = tuple(
            [vx, vy, vz, a1x, a1y, a1z, a2x, a2y, a2z, a3x, a3y, a3z]
        )

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Box`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for surface.

        Returns:
            ``Box`` object.

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

        if tokens.popl() != 'box':
            raise errors.McnpError(errors.McnpCode.UNRECOGNIZED_KEYWORD, info=source)

        vx = types.McnpReal.from_mcnp(tokens.popl())
        vy = types.McnpReal.from_mcnp(tokens.popl())
        vz = types.McnpReal.from_mcnp(tokens.popl())
        a1x = types.McnpReal.from_mcnp(tokens.popl())
        a1y = types.McnpReal.from_mcnp(tokens.popl())
        a1z = types.McnpReal.from_mcnp(tokens.popl())
        a2x = types.McnpReal.from_mcnp(tokens.popl())
        a2y = types.McnpReal.from_mcnp(tokens.popl())
        a2z = types.McnpReal.from_mcnp(tokens.popl())
        a3x = types.McnpReal.from_mcnp(tokens.popl())
        a3y = types.McnpReal.from_mcnp(tokens.popl())
        a3z = types.McnpReal.from_mcnp(tokens.popl())

        return Box(
            number,
            transform,
            vx,
            vy,
            vz,
            a1x,
            a1y,
            a1z,
            a2x,
            a2y,
            a2z,
            a3x,
            a3y,
            a3z,
            is_whiteboundary=is_whiteboundary,
            is_reflecting=is_reflecting,
        )
