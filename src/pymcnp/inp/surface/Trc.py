import re
import typing


from .option_ import SurfaceOption_
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class Trc(SurfaceOption_, keyword='trc'):
    """
    Represents INP trc elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'vx': types.Real,
        'vy': types.Real,
        'vz': types.Real,
        'hx': types.Real,
        'hy': types.Real,
        'hz': types.Real,
        'r1': types.Real,
        'r2': types.Real,
    }

    _REGEX = re.compile(
        rf'\Atrc( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})\Z'
    )

    def __init__(
        self,
        vx: types.Real,
        vy: types.Real,
        vz: types.Real,
        hx: types.Real,
        hy: types.Real,
        hz: types.Real,
        r1: types.Real,
        r2: types.Real,
    ):
        """
        Initializes ``Trc``.

        Parameters:
            vx: Truncated cone position vector x component.
            vy: Truncated cone position vector y component.
            vz: Truncated cone position vector z component.
            hx: Truncated cone height vector x component.
            hy: Truncated cone height vector y component.
            hz: Truncated cone height vector z component.
            r1: Truncated cone lower cone radius.
            r2: Truncated cone upper cone radius.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if vx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, vx)
        if vy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, vy)
        if vz is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, vz)
        if hx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, hx)
        if hy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, hy)
        if hz is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, hz)
        if r1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, r1)
        if r2 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, r2)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                vx,
                vy,
                vz,
                hx,
                hy,
                hz,
                r1,
                r2,
            ]
        )

        self.vx: typing.Final[types.Real] = vx
        self.vy: typing.Final[types.Real] = vy
        self.vz: typing.Final[types.Real] = vz
        self.hx: typing.Final[types.Real] = hx
        self.hy: typing.Final[types.Real] = hy
        self.hz: typing.Final[types.Real] = hz
        self.r1: typing.Final[types.Real] = r1
        self.r2: typing.Final[types.Real] = r2

    def draw(self):
        """
        Generates ``Visualization`` from ``Trc``.

        Returns:
            ``pyvista.PolyData`` for ``Trc``
        """

        h = _visualization.Vector(self.hx.value, self.hy.value, self.hz.value)

        cross = h * _visualization.Vector(0, 0, 1)
        angle = h & _visualization.Vector(0, 0, 1)

        vis = _visualization.Visualization.get_cone_truncated(
            h.norm(), self.r1.value, self.r2.value
        )
        vis = vis.add_rotation(cross, angle, (0, 0, 0))
        vis = vis.add_translation(
            _visualization.Vector(self.vx.value, self.vy.value, self.vz.value)
        )

        return vis
