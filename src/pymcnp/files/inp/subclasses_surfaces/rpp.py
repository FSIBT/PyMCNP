"""
Contains the ``Rpp`` subclass of ``Surface``.
"""

from typing import Final

from ..surface import Surface, SurfaceMnemonic
from ...utils import types, errors, _parser


class Rpp(Surface):
    """
    Represents INP rpp surface cards.

    ``Rpp`` implements ``Surface``.

    Attributes:
        xmin: Parallelepiped x termini minimum.
        xmax: Parallelepiped x termini maximum.
        ymin: Parallelepiped y termini minimum.
        ymax: Parallelepiped y termini maximum.
        zmin: Parallelepiped z termini minimum.
        zmax: Parallelepiped z termini maximum.
    """

    def __init__(
        self,
        number: types.McnpInteger,
        transform: types.McnpInteger,
        xmin: types.McnpReal,
        xmax: types.McnpReal,
        ymin: types.McnpReal,
        ymax: types.McnpReal,
        zmin: types.McnpReal,
        zmax: types.McnpReal,
        is_whiteboundary: bool = False,
        is_reflecting: bool = False,
    ):
        """
        Initializes ``Rpp``.


        Parameters:
            xmin: Parallelepiped x termini minimum.
            xmax: Parallelepiped x termini maximum.
            ymin: Parallelepiped y termini minimum.
            ymax: Parallelepiped y termini maximum.
            zmin: Parallelepiped z termini minimum.
            zmax: Parallelepiped z termini maximum.

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

        if xmin is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(xmin))

        if xmax is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(xmax))

        if ymin is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(ymin))

        if ymax is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(ymax))

        if zmin is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(zmin))

        if zmax is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(zmax))

        self.ident: Final[int] = number.value
        self.number: Final[types.McnpInteger] = number
        self.mnemonic: Final[SurfaceMnemonic] = SurfaceMnemonic.RPP
        self.transform: Final[types.McnpInteger] = transform
        self.is_reflecting: Final[bool] = is_reflecting
        self.is_whiteboundary: Final[bool] = is_whiteboundary

        self.xmin: Final[types.McnpReal] = xmin
        self.xmax: Final[types.McnpReal] = xmax
        self.ymin: Final[types.McnpReal] = ymin
        self.ymax: Final[types.McnpReal] = ymax
        self.zmin: Final[types.McnpReal] = zmin
        self.zmax: Final[types.McnpReal] = zmax
        self.parameters: Final[tuple[types.McnpReal]] = tuple([xmin, xmax, ymin, ymax, zmin, zmax])

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Rpp`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for surface.

        Returns:
            ``Rpp`` object.

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

        if tokens.popl() != 'rpp':
            raise errors.McnpError(errors.McnpCode.UNRECOGNIZED_KEYWORD, info=source)

        xmin = types.McnpReal.from_mcnp(tokens.popl())
        xmax = types.McnpReal.from_mcnp(tokens.popl())
        ymin = types.McnpReal.from_mcnp(tokens.popl())
        ymax = types.McnpReal.from_mcnp(tokens.popl())
        zmin = types.McnpReal.from_mcnp(tokens.popl())
        zmax = types.McnpReal.from_mcnp(tokens.popl())

        return Rpp(
            number,
            transform,
            xmin,
            xmax,
            ymin,
            ymax,
            zmin,
            zmax,
            is_whiteboundary=is_whiteboundary,
            is_reflecting=is_reflecting,
        )