import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser
from ...utils import _visualization


class SurfaceOption_P0(_option.SurfaceOption_, keyword='p'):
    """
    Represents INP surface card p_0 options.

    Attributes:
        a: Equation-defined general plane A coefficent.
        b: Equation-defined general plane B coefficent.
        c: Equation-defined general plane C coefficent.
        d: Equation-defined general plane D coefficent.
    """

    _REGEX = re.compile(r'\Ap( \S+)( \S+)( \S+)( \S+)\Z')

    def __init__(self, a: types.Real, b: types.Real, c: types.Real, d: types.Real):
        """
        Initializes ``SurfaceOption_P0``.

        Parameters:
            a: Equation-defined general plane A coefficent.
            b: Equation-defined general plane B coefficent.
            c: Equation-defined general plane C coefficent.
            d: Equation-defined general plane D coefficent.

        Returns:
            ``SurfaceOption_P0``.

        Raises:
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
        """

        if a is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, a)
        if b is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, b)
        if c is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, c)
        if d is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, d)

        self.value: typing.Final[tuple[any]] = types._Tuple([a, b, c, d])
        self.a: typing.Final[types.Real] = a
        self.b: typing.Final[types.Real] = b
        self.c: typing.Final[types.Real] = c
        self.d: typing.Final[types.Real] = d

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SurfaceOption_P0`` from INP.

        Parameters:
            source: INP surface card option.

        Returns:
            ``SurfaceOption_P0``.

        Raises:
            McnpError: SYNTAX_SURFACE_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SurfaceOption_P0._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_SURFACE_OPTION, source)

        a = types.Real.from_mcnp(tokens[1])
        b = types.Real.from_mcnp(tokens[2])
        c = types.Real.from_mcnp(tokens[3])
        d = types.Real.from_mcnp(tokens[4])

        return SurfaceOption_P0(a, b, c, d)

    def to_pyvista(self):
        """
        Generates ``pyvista.PolyData`` from ``SurfaceOption_Px``.

        Returns:
            ``pyvista.PolyData`` for ``SurfaceOption_Px``
        """

        vis = _visualization.McnpVisualization.get_plane(
            self.a.value, self.b.value, self.c.value, self.d.value
        )

        return vis.data
