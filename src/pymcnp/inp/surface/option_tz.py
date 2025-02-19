import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser
from ...utils import _visualization


class SurfaceOption_Tz(_option.SurfaceOption_, keyword='tz'):
    """
    Represents INP surface card tz options.

    Attributes:
        x: Parallel-to-z-axis tori center x component.
        y: Parallel-to-z-axis tori center y component.
        z: Parallel-to-z-axis tori center z component.
        a: Parallel-to-z-axis tori A coefficent.
        b: Parallel-to-z-axis tori B coefficent.
        c: Parallel-to-z-axis tori C coefficent.
    """

    _REGEX = re.compile(r'\Atz( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)\Z')

    def __init__(
        self,
        x: types.Real,
        y: types.Real,
        z: types.Real,
        a: types.Real,
        b: types.Real,
        c: types.Real,
    ):
        """
        Initializes ``SurfaceOption_Tz``.

        Parameters:
            x: Parallel-to-z-axis tori center x component.
            y: Parallel-to-z-axis tori center y component.
            z: Parallel-to-z-axis tori center z component.
            a: Parallel-to-z-axis tori A coefficent.
            b: Parallel-to-z-axis tori B coefficent.
            c: Parallel-to-z-axis tori C coefficent.

        Returns:
            ``SurfaceOption_Tz``.

        Raises:
            InpError: SYNTAX_OPTION_VALUE.
        """

        if x is None:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION_VALUE, x)
        if y is None:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION_VALUE, y)
        if z is None:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION_VALUE, z)
        if a is None:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION_VALUE, a)
        if b is None:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION_VALUE, b)
        if c is None:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION_VALUE, c)

        self.value: typing.Final[tuple[any]] = types._Tuple([x, y, z, a, b, c])
        self.x: typing.Final[types.Real] = x
        self.y: typing.Final[types.Real] = y
        self.z: typing.Final[types.Real] = z
        self.a: typing.Final[types.Real] = a
        self.b: typing.Final[types.Real] = b
        self.c: typing.Final[types.Real] = c

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SurfaceOption_Tz`` from INP.

        Parameters:
            source: INP surface card option.

        Returns:
            ``SurfaceOption_Tz``.

        Raises:
            InpError: SYNTAX_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SurfaceOption_Tz._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        x = types.Real.from_mcnp(tokens[1])
        y = types.Real.from_mcnp(tokens[2])
        z = types.Real.from_mcnp(tokens[3])
        a = types.Real.from_mcnp(tokens[4])
        b = types.Real.from_mcnp(tokens[5])
        c = types.Real.from_mcnp(tokens[6])

        return SurfaceOption_Tz(x, y, z, a, b, c)

    def to_pyvista(self):
        """
        Generates ``pyvista.PolyData`` from ``SurfaceOption_Tz``.

        Returns:
            ``pyvista.PolyData`` for ``SurfaceOption_Tz``
        """

        vis = _visualization.McnpVisualization.get_torus(self.b.value, self.c.value, self.a.value)
        vis = vis.add_translation(_visualization.Vector(self.x.value, self.y.value, self.z.value))

        return vis.data
