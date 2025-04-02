import re
import typing


from .option_ import SurfaceOption_
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class Box(SurfaceOption_, keyword='box'):
    """
    Represents INP box elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'vx': types.Real,
        'vy': types.Real,
        'vz': types.Real,
        'a1x': types.Real,
        'a1y': types.Real,
        'a1z': types.Real,
        'a2x': types.Real,
        'a2y': types.Real,
        'a2z': types.Real,
        'a3x': types.Real,
        'a3y': types.Real,
        'a3z': types.Real,
    }

    _REGEX = re.compile(
        rf'\Abox( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})\Z'
    )

    def __init__(
        self,
        vx: types.Real,
        vy: types.Real,
        vz: types.Real,
        a1x: types.Real,
        a1y: types.Real,
        a1z: types.Real,
        a2x: types.Real,
        a2y: types.Real,
        a2z: types.Real,
        a3x: types.Real,
        a3y: types.Real,
        a3z: types.Real,
    ):
        """
        Initializes ``Box``.

        Parameters:
            vx: Box macrobody position vector x component.
            vy: Box macrobody position vector y component.
            vz: Box macrobody position vector z component.
            a1x: Box macrobody vector #1 x component.
            a1y: Box macrobody vector #1 y component.
            a1z: Box macrobody vector #1 z component.
            a2x: Box macrobody vector #2 x component.
            a2y: Box macrobody vector #2 y component.
            a2z: Box macrobody vector #2 z component.
            a3x: Box macrobody vector #3 x component.
            a3y: Box macrobody vector #3 y component.
            a3z: Box macrobody vector #3 z component.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if vx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, vx)
        if vy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, vy)
        if vz is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, vz)
        if a1x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, a1x)
        if a1y is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, a1y)
        if a1z is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, a1z)
        if a2x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, a2x)
        if a2y is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, a2y)
        if a2z is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, a2z)
        if a3x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, a3x)
        if a3y is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, a3y)
        if a3z is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, a3z)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                vx,
                vy,
                vz,
                a1x,
                a1y,
                a1z,
                a2x,
                a2y,
                a2z,
                a3x,
                a3y,
                a3z,
            ]
        )

        self.vx: typing.Final[types.Real] = vx
        self.vy: typing.Final[types.Real] = vy
        self.vz: typing.Final[types.Real] = vz
        self.a1x: typing.Final[types.Real] = a1x
        self.a1y: typing.Final[types.Real] = a1y
        self.a1z: typing.Final[types.Real] = a1z
        self.a2x: typing.Final[types.Real] = a2x
        self.a2y: typing.Final[types.Real] = a2y
        self.a2z: typing.Final[types.Real] = a2z
        self.a3x: typing.Final[types.Real] = a3x
        self.a3y: typing.Final[types.Real] = a3y
        self.a3z: typing.Final[types.Real] = a3z

    def draw(self):
        """
        Generates ``Visualization`` from ``Box``.

        Returns:
            ``pyvista.PolyData`` for ``Box``.
        """

        v = _visualization.Vector(self.vx.value, self.vy.value, self.vz.value)
        a1 = _visualization.Vector(self.a1x.value, self.a1y.value, self.a1z.value)
        a2 = _visualization.Vector(self.a2x.value, self.a2y.value, self.a2z.value)
        a3 = _visualization.Vector(self.a3x.value, self.a3y.value, self.a3z.value)
        cross = _visualization.Vector(1, 0, 0) * a1
        angle = _visualization.Vector(1, 0, 0) & a1

        vis = _visualization.Visualization.get_box(a1.norm(), a2.norm(), a3.norm())
        vis = vis.add_rotation(cross, angle, (0, 0, 0))
        vis = vis.add_translation(v)

        return vis
