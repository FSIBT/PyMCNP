"""
Contains the ``Rhp`` subclass of ``Surface``.
"""

from typing import Final

from ..surface import Surface
from ..surface_mnemonic import SurfaceMnemonic
from ...utils import types
from ...utils import errors
from ...utils import _parser


class Rhp(Surface):
    """
    Represents INP rhp surface cards.

    ``Rhp`` implements ``Surface``.

    Attributes:
        vx: Hexagonal prism position vector x component.
        vy: Hexagonal prism position vector y component.
        vz: Hexagonal prism position vector z component.
        hx: Hexagonal prism height vector x component.
        hy: Hexagonal prism height vector y component.
        hz: Hexagonal prism height vector z component.
        r1: Hexagonal prism facet #1 vector x component.
        r2: Hexagonal prism facet #1 vector y component.
        r3: Hexagonal prism facet #1 vector z component.
        s1: Hexagonal prism facet #2 vector x component.
        s2: Hexagonal prism facet #2 vector y component.
        s3: Hexagonal prism facet #2 vector z component.
        t1: Hexagonal prism facet #3 vector x component.
        t2: Hexagonal prism facet #3 vector y component.
        t3: Hexagonal prism facet #3 vector z component.
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
        r1: types.McnpReal,
        r2: types.McnpReal,
        r3: types.McnpReal,
        s1: types.McnpReal,
        s2: types.McnpReal,
        s3: types.McnpReal,
        t1: types.McnpReal,
        t2: types.McnpReal,
        t3: types.McnpReal,
        is_whiteboundary: bool = False,
        is_reflecting: bool = False,
    ):
        """
        Initializes ``Rhp``.


        Parameters:
            vx: Hexagonal prism position vector x component.
            vy: Hexagonal prism position vector y component.
            vz: Hexagonal prism position vector z component.
            hx: Hexagonal prism height vector x component.
            hy: Hexagonal prism height vector y component.
            hz: Hexagonal prism height vector z component.
            r1: Hexagonal prism facet #1 vector x component.
            r2: Hexagonal prism facet #1 vector y component.
            r3: Hexagonal prism facet #1 vector z component.
            s1: Hexagonal prism facet #2 vector x component.
            s2: Hexagonal prism facet #2 vector y component.
            s3: Hexagonal prism facet #2 vector z component.
            t1: Hexagonal prism facet #3 vector x component.
            t2: Hexagonal prism facet #3 vector y component.
            t3: Hexagonal prism facet #3 vector z component.

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

        if r1 is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(r1))

        if r2 is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(r2))

        if r3 is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(r3))

        if s1 is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(s1))

        if s2 is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(s2))

        if s3 is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(s3))

        if t1 is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(t1))

        if t2 is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(t2))

        if t3 is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(t3))

        self.ident: Final[int] = number.value
        self.number: Final[types.McnpInteger] = number
        self.mnemonic: Final[SurfaceMnemonic] = SurfaceMnemonic.RHP
        self.transform: Final[types.McnpInteger] = transform
        self.is_reflecting: Final[bool] = is_reflecting
        self.is_whiteboundary: Final[bool] = is_whiteboundary

        self.vx: Final[types.McnpReal] = vx
        self.vy: Final[types.McnpReal] = vy
        self.vz: Final[types.McnpReal] = vz
        self.hx: Final[types.McnpReal] = hx
        self.hy: Final[types.McnpReal] = hy
        self.hz: Final[types.McnpReal] = hz
        self.r1: Final[types.McnpReal] = r1
        self.r2: Final[types.McnpReal] = r2
        self.r3: Final[types.McnpReal] = r3
        self.s1: Final[types.McnpReal] = s1
        self.s2: Final[types.McnpReal] = s2
        self.s3: Final[types.McnpReal] = s3
        self.t1: Final[types.McnpReal] = t1
        self.t2: Final[types.McnpReal] = t2
        self.t3: Final[types.McnpReal] = t3
        self.parameters: Final[tuple[types.McnpReal]] = tuple(
            [vx, vy, vz, hx, hy, hz, r1, r2, r3, s1, s2, s3, t1, t2, t3]
        )

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Rhp`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for surface.

        Returns:
            ``Rhp`` object.

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

        if tokens.popl() != 'rhp':
            raise errors.McnpError(errors.McnpCode.UNRECOGNIZED_KEYWORD, info=source)

        vx = types.McnpReal.from_mcnp(tokens.popl())
        vy = types.McnpReal.from_mcnp(tokens.popl())
        vz = types.McnpReal.from_mcnp(tokens.popl())
        hx = types.McnpReal.from_mcnp(tokens.popl())
        hy = types.McnpReal.from_mcnp(tokens.popl())
        hz = types.McnpReal.from_mcnp(tokens.popl())
        r1 = types.McnpReal.from_mcnp(tokens.popl())
        r2 = types.McnpReal.from_mcnp(tokens.popl())
        r3 = types.McnpReal.from_mcnp(tokens.popl())
        s1 = types.McnpReal.from_mcnp(tokens.popl())
        s2 = types.McnpReal.from_mcnp(tokens.popl())
        s3 = types.McnpReal.from_mcnp(tokens.popl())
        t1 = types.McnpReal.from_mcnp(tokens.popl())
        t2 = types.McnpReal.from_mcnp(tokens.popl())
        t3 = types.McnpReal.from_mcnp(tokens.popl())

        return Rhp(
            number,
            transform,
            vx,
            vy,
            vz,
            hx,
            hy,
            hz,
            r1,
            r2,
            r3,
            s1,
            s2,
            s3,
            t1,
            t2,
            t3,
            is_whiteboundary=is_whiteboundary,
            is_reflecting=is_reflecting,
        )