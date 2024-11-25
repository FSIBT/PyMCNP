"""
Contains the ``Wed`` subclass of ``Surface``.
"""

from typing import Final

from ..surface import Surface, SurfaceMnemonic
from ...utils import types, errors, _parser


class Wed(Surface):
    """
    Represents INP wed surface cards.

    ``Wed`` implements ``Surface``.

    Attributes:
        vx: Wedge position vector x component.
        vy: Wedge position vector y component.
        vz: Wedge position vector z component.
        v1x: Wedge side vector #1 x component.
        v1y: Wedge side vector #1 y component.
        v1z: Wedge side vector #1 z component.
        v2x: Wedge side vector #2 x component.
        v2y: Wedge side vector #2 y component.
        v2z: Wedge side vector #2 z component.
        v3x: Wedge height vector x component.
        v3y: Wedge height vector y component.
        v3z: Wedge height vector z component.
    """

    def __init__(
        self,
        number: types.McnpInteger,
        transform: types.McnpInteger,
        vx: types.McnpReal,
        vy: types.McnpReal,
        vz: types.McnpReal,
        v1x: types.McnpReal,
        v1y: types.McnpReal,
        v1z: types.McnpReal,
        v2x: types.McnpReal,
        v2y: types.McnpReal,
        v2z: types.McnpReal,
        v3x: types.McnpReal,
        v3y: types.McnpReal,
        v3z: types.McnpReal,
        is_whiteboundary: bool = False,
        is_reflecting: bool = False,
    ):
        """
        Initializes ``Wed``.


        Parameters:
            vx: Wedge position vector x component.
            vy: Wedge position vector y component.
            vz: Wedge position vector z component.
            v1x: Wedge side vector #1 x component.
            v1y: Wedge side vector #1 y component.
            v1z: Wedge side vector #1 z component.
            v2x: Wedge side vector #2 x component.
            v2y: Wedge side vector #2 y component.
            v2z: Wedge side vector #2 z component.
            v3x: Wedge height vector x component.
            v3y: Wedge height vector y component.
            v3z: Wedge height vector z component.

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

        if v1x is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(v1x))

        if v1y is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(v1y))

        if v1z is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(v1z))

        if v2x is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(v2x))

        if v2y is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(v2y))

        if v2z is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(v2z))

        if v3x is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(v3x))

        if v3y is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(v3y))

        if v3z is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(v3z))

        self.ident: Final[int] = number.value
        self.number: Final[types.McnpInteger] = number
        self.mnemonic: Final[SurfaceMnemonic] = SurfaceMnemonic.WED
        self.transform: Final[types.McnpInteger] = transform
        self.is_reflecting: Final[bool] = is_reflecting
        self.is_whiteboundary: Final[bool] = is_whiteboundary

        self.vx: Final[types.McnpReal] = vx
        self.vy: Final[types.McnpReal] = vy
        self.vz: Final[types.McnpReal] = vz
        self.v1x: Final[types.McnpReal] = v1x
        self.v1y: Final[types.McnpReal] = v1y
        self.v1z: Final[types.McnpReal] = v1z
        self.v2x: Final[types.McnpReal] = v2x
        self.v2y: Final[types.McnpReal] = v2y
        self.v2z: Final[types.McnpReal] = v2z
        self.v3x: Final[types.McnpReal] = v3x
        self.v3y: Final[types.McnpReal] = v3y
        self.v3z: Final[types.McnpReal] = v3z
        self.parameters: Final[tuple[types.McnpReal]] = tuple(
            [vx, vy, vz, v1x, v1y, v1z, v2x, v2y, v2z, v3x, v3y, v3z]
        )

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Wed`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for surface.

        Returns:
            ``Wed`` object.

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

        if tokens.popl() != 'wed':
            raise errors.McnpError(errors.McnpCode.UNRECOGNIZED_KEYWORD, info=source)

        vx = types.McnpReal.from_mcnp(tokens.popl())
        vy = types.McnpReal.from_mcnp(tokens.popl())
        vz = types.McnpReal.from_mcnp(tokens.popl())
        v1x = types.McnpReal.from_mcnp(tokens.popl())
        v1y = types.McnpReal.from_mcnp(tokens.popl())
        v1z = types.McnpReal.from_mcnp(tokens.popl())
        v2x = types.McnpReal.from_mcnp(tokens.popl())
        v2y = types.McnpReal.from_mcnp(tokens.popl())
        v2z = types.McnpReal.from_mcnp(tokens.popl())
        v3x = types.McnpReal.from_mcnp(tokens.popl())
        v3y = types.McnpReal.from_mcnp(tokens.popl())
        v3z = types.McnpReal.from_mcnp(tokens.popl())

        return Wed(
            number,
            transform,
            vx,
            vy,
            vz,
            v1x,
            v1y,
            v1z,
            v2x,
            v2y,
            v2z,
            v3x,
            v3y,
            v3z,
            is_whiteboundary=is_whiteboundary,
            is_reflecting=is_reflecting,
        )
