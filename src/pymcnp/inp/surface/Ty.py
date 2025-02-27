import re
import typing


from .option_ import SurfaceOption_
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class Ty(SurfaceOption_, keyword='ty'):
    """
    Represents INP ty elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'x': types.Real,
        'y': types.Real,
        'z': types.Real,
        'a': types.Real,
        'b': types.Real,
        'c': types.Real,
    }

    _REGEX = re.compile(r'ty( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)')

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
        Initializes ``Ty``.

        Parameters:
            x: Parallel-to-y-axis tori center x component.
            y: Parallel-to-y-axis tori center y component.
            z: Parallel-to-y-axis tori center z component.
            a: Parallel-to-y-axis tori A coefficent.
            b: Parallel-to-y-axis tori B coefficent.
            c: Parallel-to-y-axis tori C coefficent.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x)
        if y is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, y)
        if z is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, z)
        if a is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, a)
        if b is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, b)
        if c is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, c)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                x,
                y,
                z,
                a,
                b,
                c,
            ]
        )

        self.x: typing.Final[types.Real] = x
        self.y: typing.Final[types.Real] = y
        self.z: typing.Final[types.Real] = z
        self.a: typing.Final[types.Real] = a
        self.b: typing.Final[types.Real] = b
        self.c: typing.Final[types.Real] = c

        def to_pyvista(self):
            """
            Generates ``pyvista.PolyData`` from ``Ty``.

            Returns:
                ``pyvista.PolyData`` for ``Ty``
            """

            vis = _visualization.McnpVisualization.get_torus(
                self.b.value, self.c.value, self.a.value
            )
            vis = vis.add_rotation(_visualization.Vector(1, 0, 0), 90, (0, 0, 0))
            vis = vis.add_translation(
                _visualization.Vector(self.x.value, self.y.value, self.z.value)
            )

            return vis.data
