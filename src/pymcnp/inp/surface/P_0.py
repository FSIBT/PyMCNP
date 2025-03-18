import re
import typing


from .option_ import SurfaceOption_
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class P_0(SurfaceOption_, keyword='p'):
    """
    Represents INP p_0 elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'a': types.Real,
        'b': types.Real,
        'c': types.Real,
        'd': types.Real,
    }

    _REGEX = re.compile(
        rf'p( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})'
    )

    def __init__(self, a: types.Real, b: types.Real, c: types.Real, d: types.Real):
        """
        Initializes ``P_0``.

        Parameters:
            a: Equation-defined general plane A coefficent.
            b: Equation-defined general plane B coefficent.
            c: Equation-defined general plane C coefficent.
            d: Equation-defined general plane D coefficent.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if a is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, a)
        if b is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, b)
        if c is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, c)
        if d is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, d)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                a,
                b,
                c,
                d,
            ]
        )

        self.a: typing.Final[types.Real] = a
        self.b: typing.Final[types.Real] = b
        self.c: typing.Final[types.Real] = c
        self.d: typing.Final[types.Real] = d

    def draw(self):
        """
        Generates ``Visualization`` from ``Px``.

        Returns:
            ``pyvista.PolyData`` for ``Px``
        """

        vis = _visualization.Visualization.get_plane(
            self.a.value, self.b.value, self.c.value, self.d.value
        )

        return vis
