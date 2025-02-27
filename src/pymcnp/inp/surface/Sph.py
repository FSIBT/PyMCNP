import re
import typing


from .option_ import SurfaceOption_
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class Sph(SurfaceOption_, keyword='sph'):
    """
    Represents INP sph elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'vx': types.Real,
        'vy': types.Real,
        'vz': types.Real,
        'r': types.Real,
    }

    _REGEX = re.compile(r'sph( \S+)( \S+)( \S+)( \S+)')

    def __init__(self, vx: types.Real, vy: types.Real, vz: types.Real, r: types.Real):
        """
        Initializes ``Sph``.

        Parameters:
            vx: Sphere macrobody position vector x component.
            vy: Sphere macrobody position vector y component.
            vz: Sphere macrobody position vector z component.
            r: Sphere macrobody radius.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if vx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, vx)
        if vy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, vy)
        if vz is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, vz)
        if r is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, r)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                vx,
                vy,
                vz,
                r,
            ]
        )

        self.vx: typing.Final[types.Real] = vx
        self.vy: typing.Final[types.Real] = vy
        self.vz: typing.Final[types.Real] = vz
        self.r: typing.Final[types.Real] = r

        def to_pyvista(self):
            """
            Generates ``pyvista.PolyData`` from ``Sph``.

            Returns:
                ``pyvista.PolyData`` for ``Sph``
            """

            vis = _visualization.McnpVisualization.get_sphere(self.r.value)
            vis = vis.add_translation(
                _visualization.Vector(self.vx.value, self.vy.value, self.vz.value)
            )

            return vis.data
