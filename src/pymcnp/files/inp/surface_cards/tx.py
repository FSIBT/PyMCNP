"""
Contains the ``Tx`` subclass of ``Surface``.
"""

from typing import Final

from ..surface import Surface
from ..surface_mnemonic import SurfaceMnemonic
from ...utils import _visualization
from ...utils import types
from ...utils import errors
from ...utils import _parser


class Tx(Surface):
    """
    Represents INP tx surface cards.

    ``Tx`` implements ``Surface``.

    Attributes:
        x: Parallel-to-x-axis tori center x component.
        y: Parallel-to-x-axis tori center y component.
        z: Parallel-to-x-axis tori center z component.
        a: Parallel-to-x-axis tori A coefficent.
        b: Parallel-to-x-axis tori B coefficent.
        c: Parallel-to-x-axis tori C coefficent.
    """

    def __init__(
        self,
        number: types.McnpInteger,
        transform: types.McnpInteger,
        x: types.McnpReal,
        y: types.McnpReal,
        z: types.McnpReal,
        a: types.McnpReal,
        b: types.McnpReal,
        c: types.McnpReal,
        is_whiteboundary: bool = False,
        is_reflecting: bool = False,
    ):
        """
        Initializes ``Tx``.

        Parameters:
            x: Parallel-to-x-axis tori center x component.
            y: Parallel-to-x-axis tori center y component.
            z: Parallel-to-x-axis tori center z component.
            a: Parallel-to-x-axis tori A coefficent.
            b: Parallel-to-x-axis tori B coefficent.
            c: Parallel-to-x-axis tori C coefficent.

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

        if x is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(x))

        if y is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(y))

        if z is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(z))

        if a is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(a))

        if b is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(b))

        if c is None:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str(c))

        self.ident: Final[int] = number.value
        self.number: Final[types.McnpInteger] = number
        self.mnemonic: Final[SurfaceMnemonic] = SurfaceMnemonic.TX
        self.transform: Final[types.McnpInteger] = transform
        self.is_reflecting: Final[bool] = is_reflecting
        self.is_whiteboundary: Final[bool] = is_whiteboundary

        self.x: Final[types.McnpReal] = x
        self.y: Final[types.McnpReal] = y
        self.z: Final[types.McnpReal] = z
        self.a: Final[types.McnpReal] = a
        self.b: Final[types.McnpReal] = b
        self.c: Final[types.McnpReal] = c
        self.parameters: Final[tuple[types.McnpReal]] = tuple([x, y, z, a, b, c])

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Tx`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for surface.

        Returns:
            ``Tx`` object.

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

        if tokens.popl() != 'tx':
            raise errors.McnpError(errors.McnpCode.UNRECOGNIZED_KEYWORD, info=source)

        x = types.McnpReal.from_mcnp(tokens.popl())
        y = types.McnpReal.from_mcnp(tokens.popl())
        z = types.McnpReal.from_mcnp(tokens.popl())
        a = types.McnpReal.from_mcnp(tokens.popl())
        b = types.McnpReal.from_mcnp(tokens.popl())
        c = types.McnpReal.from_mcnp(tokens.popl())

        return Tx(
            number,
            transform,
            x,
            y,
            z,
            a,
            b,
            c,
            is_whiteboundary=is_whiteboundary,
            is_reflecting=is_reflecting,
        )

    def to_pyvista(self):
        """
        Generates ``pyvista.PolyData`` representing ``Tx``.

        Returns:
            ``pyvista.PolyData`` for ``Tx``.
        """

        vis = _visualization.PyMcnpVisualization.get_torus(self.b.value, self.c.value, self.a.value)
        vis = vis.add_rotation(_visualization.Vector(0, 1, 0), 90, (0, 0, 0))
        vis = vis.add_translation(_visualization.Vector(self.x.value, self.y.value, self.z.value))

        return vis.data
