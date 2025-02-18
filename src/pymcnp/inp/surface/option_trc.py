import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser
from ...utils import _visualization


class SurfaceOption_Trc(_option.SurfaceOption_, keyword='trc'):
    """
    Represents INP surface card trc options.

    Attributes:
        vx: Truncated cone position vector x component.
        vy: Truncated cone position vector y component.
        vz: Truncated cone position vector z component.
        hx: Truncated cone height vector x component.
        hy: Truncated cone height vector y component.
        hz: Truncated cone height vector z component.
        r1: Truncated cone lower cone radius.
        r2: Truncated cone upper cone radius.
    """

    _REGEX = re.compile(r'\Atrc( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)\Z')

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
        Initializes ``SurfaceOption_Trc``.

        Parameters:
            vx: Truncated cone position vector x component.
            vy: Truncated cone position vector y component.
            vz: Truncated cone position vector z component.
            hx: Truncated cone height vector x component.
            hy: Truncated cone height vector y component.
            hz: Truncated cone height vector z component.
            r1: Truncated cone lower cone radius.
            r2: Truncated cone upper cone radius.

        Returns:
            ``SurfaceOption_Trc``.

        Raises:
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
        """

        if vx is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, vx)
        if vy is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, vy)
        if vz is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, vz)
        if hx is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, hx)
        if hy is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, hy)
        if hz is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, hz)
        if r1 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, r1)
        if r2 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, r2)

        self.value: typing.Final[tuple[any]] = types._Tuple([vx, vy, vz, hx, hy, hz, r1, r2])
        self.vx: typing.Final[types.Real] = vx
        self.vy: typing.Final[types.Real] = vy
        self.vz: typing.Final[types.Real] = vz
        self.hx: typing.Final[types.Real] = hx
        self.hy: typing.Final[types.Real] = hy
        self.hz: typing.Final[types.Real] = hz
        self.r1: typing.Final[types.Real] = r1
        self.r2: typing.Final[types.Real] = r2

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SurfaceOption_Trc`` from INP.

        Parameters:
            source: INP surface card option.

        Returns:
            ``SurfaceOption_Trc``.

        Raises:
            McnpError: SYNTAX_SURFACE_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SurfaceOption_Trc._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_SURFACE_OPTION, source)

        vx = types.Real.from_mcnp(tokens[1])
        vy = types.Real.from_mcnp(tokens[2])
        vz = types.Real.from_mcnp(tokens[3])
        hx = types.Real.from_mcnp(tokens[4])
        hy = types.Real.from_mcnp(tokens[5])
        hz = types.Real.from_mcnp(tokens[6])
        r1 = types.Real.from_mcnp(tokens[7])
        r2 = types.Real.from_mcnp(tokens[8])

        return SurfaceOption_Trc(vx, vy, vz, hx, hy, hz, r1, r2)

    def to_pyvista(self):
        """
        Generates ``pyvista.PolyData`` from ``SurfaceOption_Trc``.

        Returns:
            ``pyvista.PolyData`` for ``SurfaceOption_Trc``
        """

        h = _visualization.Vector(self.hx.value, self.hy.value, self.hz.value)

        cross = h * _visualization.Vector(0, 0, 1)
        angle = h & _visualization.Vector(0, 0, 1)

        vis = _visualization.McnpVisualization.get_cone_truncated(
            h.norm(), self.r1.value, self.r2.value
        )
        vis = vis.add_rotation(cross, angle, (0, 0, 0))
        vis = vis.add_translation(
            _visualization.Vector(self.vx.value, self.vy.value, self.vz.value)
        )

        return vis.data
