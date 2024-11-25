"""
Contains the ``Rec`` subclass of ``Surface``.
"""

from typing import Final

from ..surface import Surface, SurfaceMnemonic
from ...utils import types, errors, _parser


class Rec(Surface):
    """
    Represents INP rec surface cards.

    ``Rec`` implements ``Surface``.

    Attributes:
        vx: Elliptical cylinder position vector x component.
        vy: Elliptical cylinder position vector y component.
        vz: Elliptical cylinder position vector z component.
        hx: Elliptical cylinder height vector x component.
        hy: Elliptical cylinder height vector y component.
        hz: Elliptical cylinder height vector z component.
        v1x: Elliptical cylinder major axis vector x component.
        v1y: Elliptical cylinder major axis vector y component.
        v1z: Elliptical cylinder major axis vector z component.
        v2x: Elliptical cylinder minor axis vector x component.
        v2y: Elliptical cylinder minor axis vector y component.
        v2z: Elliptical cylinder minor axis vector z component.
    """

    def __init__(
        self,
        number: types.McnpInteger,
        transform: types.McnpInteger,
        vx: types.McnpReal,
        vy: types.McnpReal,
        vz: types.McnpReal,
        hx: types.McnpReal,
        hy: types.McnpReal,
        hz: types.McnpReal,
        v1x: types.McnpReal,
        v1y: types.McnpReal,
        v1z: types.McnpReal,
        v2x: types.McnpReal,
        v2y: types.McnpReal,
        v2z: types.McnpReal,
        is_whiteboundary: bool = False,
        is_reflecting: bool = False,
    ):
        """
        Initializes ``Rec``.


        Parameters:
            vx: Elliptical cylinder position vector x component.
            vy: Elliptical cylinder position vector y component.
            vz: Elliptical cylinder position vector z component.
            hx: Elliptical cylinder height vector x component.
            hy: Elliptical cylinder height vector y component.
            hz: Elliptical cylinder height vector z component.
            v1x: Elliptical cylinder major axis vector x component.
            v1y: Elliptical cylinder major axis vector y component.
            v1z: Elliptical cylinder major axis vector z component.
            v2x: Elliptical cylinder minor axis vector x component.
            v2y: Elliptical cylinder minor axis vector y component.
            v2z: Elliptical cylinder minor axis vector z component.

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

        if hx is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(hx))

        if hy is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(hy))

        if hz is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(hz))

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

        self.ident: Final[int] = number.value
        self.number: Final[types.McnpInteger] = number
        self.mnemonic: Final[SurfaceMnemonic] = SurfaceMnemonic.REC
        self.transform: Final[types.McnpInteger] = transform
        self.is_reflecting: Final[bool] = is_reflecting
        self.is_whiteboundary: Final[bool] = is_whiteboundary

        self.vx: Final[types.McnpReal] = vx
        self.vy: Final[types.McnpReal] = vy
        self.vz: Final[types.McnpReal] = vz
        self.hx: Final[types.McnpReal] = hx
        self.hy: Final[types.McnpReal] = hy
        self.hz: Final[types.McnpReal] = hz
        self.v1x: Final[types.McnpReal] = v1x
        self.v1y: Final[types.McnpReal] = v1y
        self.v1z: Final[types.McnpReal] = v1z
        self.v2x: Final[types.McnpReal] = v2x
        self.v2y: Final[types.McnpReal] = v2y
        self.v2z: Final[types.McnpReal] = v2z
        self.parameters: Final[tuple[types.McnpReal]] = tuple(
            [vx, vy, vz, hx, hy, hz, v1x, v1y, v1z, v2x, v2y, v2z]
        )

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Rec`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for surface.

        Returns:
            ``Rec`` object.

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

        if tokens.popl() != 'rec':
            raise errors.McnpError(errors.McnpCode.UNRECOGNIZED_KEYWORD, info=source)

        vx = types.McnpReal.from_mcnp(tokens.popl())
        vy = types.McnpReal.from_mcnp(tokens.popl())
        vz = types.McnpReal.from_mcnp(tokens.popl())
        hx = types.McnpReal.from_mcnp(tokens.popl())
        hy = types.McnpReal.from_mcnp(tokens.popl())
        hz = types.McnpReal.from_mcnp(tokens.popl())
        v1x = types.McnpReal.from_mcnp(tokens.popl())
        v1y = types.McnpReal.from_mcnp(tokens.popl())
        v1z = types.McnpReal.from_mcnp(tokens.popl())
        v2x = types.McnpReal.from_mcnp(tokens.popl())
        v2y = types.McnpReal.from_mcnp(tokens.popl())
        v2z = types.McnpReal.from_mcnp(tokens.popl())

        return Rec(
            number,
            transform,
            vx,
            vy,
            vz,
            hx,
            hy,
            hz,
            v1x,
            v1y,
            v1z,
            v2x,
            v2y,
            v2z,
            is_whiteboundary=is_whiteboundary,
            is_reflecting=is_reflecting,
        )
