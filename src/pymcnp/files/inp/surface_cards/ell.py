"""
Contains the ``Ell`` subclass of ``Surface``.
"""

from typing import Final

from ..surface import Surface
from ..surface_mnemonic import SurfaceMnemonic
from ...utils import types, errors, _parser


class Ell(Surface):
    """
    Represents INP ell surface cards.

    ``Ell`` implements ``Surface``.

    Attributes:
        v1x: Ellipsoid focus #1 or center x component.
        v1y: Ellipsoid focus #1 or center y component.
        v1z: Ellipsoid focus #1 or center z component.
        v2x: Ellipsoid focus #2 or major axis x component.
        v2y: Ellipsoid focus #2 or major axis y component.
        v2z: Ellipsoid focus #2 or major axis z component.
        rm: Ellipsoid major/minor axis radius length.
    """

    def __init__(
        self,
        number: types.McnpInteger,
        transform: types.McnpInteger,
        v1x: types.McnpReal,
        v1y: types.McnpReal,
        v1z: types.McnpReal,
        v2x: types.McnpReal,
        v2y: types.McnpReal,
        v2z: types.McnpReal,
        rm: types.McnpReal,
        is_whiteboundary: bool = False,
        is_reflecting: bool = False,
    ):
        """
        Initializes ``Ell``.


        Parameters:
            v1x: Ellipsoid focus #1 or center x component.
            v1y: Ellipsoid focus #1 or center y component.
            v1z: Ellipsoid focus #1 or center z component.
            v2x: Ellipsoid focus #2 or major axis x component.
            v2y: Ellipsoid focus #2 or major axis y component.
            v2z: Ellipsoid focus #2 or major axis z component.
            rm: Ellipsoid major/minor axis radius length.

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

        if rm is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(rm))

        self.ident: Final[int] = number.value
        self.number: Final[types.McnpInteger] = number
        self.mnemonic: Final[SurfaceMnemonic] = SurfaceMnemonic.ELL
        self.transform: Final[types.McnpInteger] = transform
        self.is_reflecting: Final[bool] = is_reflecting
        self.is_whiteboundary: Final[bool] = is_whiteboundary

        self.v1x: Final[types.McnpReal] = v1x
        self.v1y: Final[types.McnpReal] = v1y
        self.v1z: Final[types.McnpReal] = v1z
        self.v2x: Final[types.McnpReal] = v2x
        self.v2y: Final[types.McnpReal] = v2y
        self.v2z: Final[types.McnpReal] = v2z
        self.rm: Final[types.McnpReal] = rm
        self.parameters: Final[tuple[types.McnpReal]] = tuple([v1x, v1y, v1z, v2x, v2y, v2z, rm])

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Ell`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for surface.

        Returns:
            ``Ell`` object.

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

        if tokens.popl() != 'ell':
            raise errors.McnpError(errors.McnpCode.UNRECOGNIZED_KEYWORD, info=source)

        v1x = types.McnpReal.from_mcnp(tokens.popl())
        v1y = types.McnpReal.from_mcnp(tokens.popl())
        v1z = types.McnpReal.from_mcnp(tokens.popl())
        v2x = types.McnpReal.from_mcnp(tokens.popl())
        v2y = types.McnpReal.from_mcnp(tokens.popl())
        v2z = types.McnpReal.from_mcnp(tokens.popl())
        rm = types.McnpReal.from_mcnp(tokens.popl())

        return Ell(
            number,
            transform,
            v1x,
            v1y,
            v1z,
            v2x,
            v2y,
            v2z,
            rm,
            is_whiteboundary=is_whiteboundary,
            is_reflecting=is_reflecting,
        )
