import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class Rcc(_option.SurfaceOption):
    """
    Represents INP rcc elements.

    Attributes:
        vx: Circular cylinder macrobody position vector x component.
        vy: Circular cylinder macrobody position vector y component.
        vz: Circular cylinder macrobody position vector z component.
        hx: Circular cylinder macrobody height vector x component.
        hy: Circular cylinder macrobody height vector y component.
        hz: Circular cylinder macrobody height vector z component.
        r: Circular cylinder macrobody radius.
    """

    _KEYWORD = 'rcc'

    _ATTRS = {
        'vx': types.Real,
        'vy': types.Real,
        'vz': types.Real,
        'hx': types.Real,
        'hy': types.Real,
        'hz': types.Real,
        'r': types.Real,
    }

    _REGEX = re.compile(
        rf'\Arcc( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z'
    )

    def __init__(self, vx: types.Real, vy: types.Real, vz: types.Real, hx: types.Real, hy: types.Real, hz: types.Real, r: types.Real):
        """
        Initializes ``Rcc``.

        Parameters:
            vx: Circular cylinder macrobody position vector x component.
            vy: Circular cylinder macrobody position vector y component.
            vz: Circular cylinder macrobody position vector z component.
            hx: Circular cylinder macrobody height vector x component.
            hy: Circular cylinder macrobody height vector y component.
            hz: Circular cylinder macrobody height vector z component.
            r: Circular cylinder macrobody radius.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if vx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, vx)
        if vy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, vy)
        if vz is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, vz)
        if hx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, hx)
        if hy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, hy)
        if hz is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, hz)
        if r is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, r)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                vx,
                vy,
                vz,
                hx,
                hy,
                hz,
                r,
            ]
        )

        self.vx: typing.Final[types.Real] = vx
        self.vy: typing.Final[types.Real] = vy
        self.vz: typing.Final[types.Real] = vz
        self.hx: typing.Final[types.Real] = hx
        self.hy: typing.Final[types.Real] = hy
        self.hz: typing.Final[types.Real] = hz
        self.r: typing.Final[types.Real] = r

    def draw(self):
        """
        Generates ``Visualization`` from ``Rcc``.

        Returns:
            ``pyvista.PolyData`` for ``Rcc``
        """

        v = _visualization.Vector(self.vx.value, self.vy.value, self.vz.value)
        h = _visualization.Vector(self.hx.value, self.hy.value, self.hz.value)

        cross = v * _visualization.Vector(0, 0, 1)
        angle = v & _visualization.Vector(0, 0, 1)

        vis = _visualization.Visualization.get_cylinder_circle(h.norm(), self.r.value)
        vis = vis.add_rotation(cross, angle, (0, 0, 0))
        vis = vis.add_translation(v)

        return vis


@dataclasses.dataclass
class RccBuilder(_option.SurfaceOptionBuilder):
    """
    Builds ``Rcc``.

    Attributes:
        vx: Circular cylinder macrobody position vector x component.
        vy: Circular cylinder macrobody position vector y component.
        vz: Circular cylinder macrobody position vector z component.
        hx: Circular cylinder macrobody height vector x component.
        hy: Circular cylinder macrobody height vector y component.
        hz: Circular cylinder macrobody height vector z component.
        r: Circular cylinder macrobody radius.
    """

    vx: str | float | types.Real
    vy: str | float | types.Real
    vz: str | float | types.Real
    hx: str | float | types.Real
    hy: str | float | types.Real
    hz: str | float | types.Real
    r: str | float | types.Real

    def build(self):
        """
        Builds ``RccBuilder`` into ``Rcc``.

        Returns:
            ``Rcc`` for ``RccBuilder``.
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

        hx = self.hx
        if isinstance(self.hx, types.Real):
            hx = self.hx
        elif isinstance(self.hx, float) or isinstance(self.hx, int):
            hx = types.Real(self.hx)
        elif isinstance(self.hx, str):
            hx = types.Real.from_mcnp(self.hx)

        hy = self.hy
        if isinstance(self.hy, types.Real):
            hy = self.hy
        elif isinstance(self.hy, float) or isinstance(self.hy, int):
            hy = types.Real(self.hy)
        elif isinstance(self.hy, str):
            hy = types.Real.from_mcnp(self.hy)

        hz = self.hz
        if isinstance(self.hz, types.Real):
            hz = self.hz
        elif isinstance(self.hz, float) or isinstance(self.hz, int):
            hz = types.Real(self.hz)
        elif isinstance(self.hz, str):
            hz = types.Real.from_mcnp(self.hz)

        r = self.r
        if isinstance(self.r, types.Real):
            r = self.r
        elif isinstance(self.r, float) or isinstance(self.r, int):
            r = types.Real(self.r)
        elif isinstance(self.r, str):
            r = types.Real.from_mcnp(self.r)

        return Rcc(
            vx=vx,
            vy=vy,
            vz=vz,
            hx=hx,
            hy=hy,
            hz=hz,
            r=r,
        )

    @staticmethod
    def unbuild(ast: Rcc):
        """
        Unbuilds ``Rcc`` into ``RccBuilder``

        Returns:
            ``RccBuilder`` for ``Rcc``.
        """

        return RccBuilder(
            vx=copy.deepcopy(ast.vx),
            vy=copy.deepcopy(ast.vy),
            vz=copy.deepcopy(ast.vz),
            hx=copy.deepcopy(ast.hx),
            hy=copy.deepcopy(ast.hy),
            hz=copy.deepcopy(ast.hz),
            r=copy.deepcopy(ast.r),
        )
