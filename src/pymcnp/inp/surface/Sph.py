import re
import copy
import typing
import dataclasses


from ._option import SurfaceOption
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class Sph(SurfaceOption):
    """
    Represents INP sph elements.

    Attributes:
        vx: Sphere macrobody position vector x component.
        vy: Sphere macrobody position vector y component.
        vz: Sphere macrobody position vector z component.
        r: Sphere macrobody radius.
    """

    _KEYWORD = 'sph'

    _ATTRS = {
        'vx': types.Real,
        'vy': types.Real,
        'vz': types.Real,
        'r': types.Real,
    }

    _REGEX = re.compile(
        rf'\Asph( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z'
    )

    def __init__(self, vx: types.Real, vy: types.Real, vz: types.Real, r: types.Real):
        """
        Initializes ``Sph``.

        Parameters:
            vx: Sphere macrobody position vector x component.
            vy: Sphere macrobody position vector y component.
            vz: Sphere macrobody position vector z component.
            r: Sphere macrobody radius.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if vx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, vx)
        if vy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, vy)
        if vz is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, vz)
        if r is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, r)

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

    def draw(self):
        """
        Generates ``Visualization`` from ``Sph``.

        Returns:
            ``pyvista.PolyData`` for ``Sph``
        """

        vis = _visualization.Visualization.get_sphere(self.r.value)
        vis = vis.add_translation(
            _visualization.Vector(self.vx.value, self.vy.value, self.vz.value)
        )

        return vis


@dataclasses.dataclass
class SphBuilder:
    """
    Builds ``Sph``.

    Attributes:
        vx: Sphere macrobody position vector x component.
        vy: Sphere macrobody position vector y component.
        vz: Sphere macrobody position vector z component.
        r: Sphere macrobody radius.
    """

    vx: str | float | types.Real
    vy: str | float | types.Real
    vz: str | float | types.Real
    r: str | float | types.Real

    def build(self):
        """
        Builds ``SphBuilder`` into ``Sph``.

        Returns:
            ``Sph`` for ``SphBuilder``.
        """

        vx = self.vx
        if isinstance(self.vx, types.Real):
            vx = self.vx
        elif isinstance(self.vx, float) or isinstance(self.vx, int):
            vx = types.Real(self.vx)
        elif isinstance(self.vx, str):
            vx = types.Real.from_mcnp(self.vx)

        vy = self.vy
        if isinstance(self.vy, types.Real):
            vy = self.vy
        elif isinstance(self.vy, float) or isinstance(self.vy, int):
            vy = types.Real(self.vy)
        elif isinstance(self.vy, str):
            vy = types.Real.from_mcnp(self.vy)

        vz = self.vz
        if isinstance(self.vz, types.Real):
            vz = self.vz
        elif isinstance(self.vz, float) or isinstance(self.vz, int):
            vz = types.Real(self.vz)
        elif isinstance(self.vz, str):
            vz = types.Real.from_mcnp(self.vz)

        r = self.r
        if isinstance(self.r, types.Real):
            r = self.r
        elif isinstance(self.r, float) or isinstance(self.r, int):
            r = types.Real(self.r)
        elif isinstance(self.r, str):
            r = types.Real.from_mcnp(self.r)

        return Sph(
            vx=vx,
            vy=vy,
            vz=vz,
            r=r,
        )

    @staticmethod
    def unbuild(ast: Sph):
        """
        Unbuilds ``Sph`` into ``SphBuilder``

        Returns:
            ``SphBuilder`` for ``Sph``.
        """

        return Sph(
            vx=copy.deepcopy(ast.vx),
            vy=copy.deepcopy(ast.vy),
            vz=copy.deepcopy(ast.vz),
            r=copy.deepcopy(ast.r),
        )
