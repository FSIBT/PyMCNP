import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class S(_option.SurfaceOption):
    """
    Represents INP s elements.

    Attributes:
        x: General sphere center x component.
        y: General sphere center y component.
        z: General sphere center z component.
        r: General sphere radius.
    """

    _KEYWORD = 's'

    _ATTRS = {
        'x': types.Real,
        'y': types.Real,
        'z': types.Real,
        'r': types.Real,
    }

    _REGEX = re.compile(rf'\As( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, x: types.Real, y: types.Real, z: types.Real, r: types.Real):
        """
        Initializes ``S``.

        Parameters:
            x: General sphere center x component.
            y: General sphere center y component.
            z: General sphere center z component.
            r: General sphere radius.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x)
        if y is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, y)
        if z is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, z)
        if r is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, r)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                x,
                y,
                z,
                r,
            ]
        )

        self.x: typing.Final[types.Real] = x
        self.y: typing.Final[types.Real] = y
        self.z: typing.Final[types.Real] = z
        self.r: typing.Final[types.Real] = r

    def draw(self):
        """
        Generates ``Visualization`` from ``S``.

        Returns:
            ``pyvista.PolyData`` for ``S``
        """

        vis = _visualization.Visualization.get_sphere(self.r.value)
        vis = vis.add_translation(_visualization.Vector(self.x.value, self.y.value, self.z.value))

        return vis


@dataclasses.dataclass
class SBuilder(_option.SurfaceOptionBuilder):
    """
    Builds ``S``.

    Attributes:
        x: General sphere center x component.
        y: General sphere center y component.
        z: General sphere center z component.
        r: General sphere radius.
    """

    x: str | float | types.Real
    y: str | float | types.Real
    z: str | float | types.Real
    r: str | float | types.Real

    def build(self):
        """
        Builds ``SBuilder`` into ``S``.

        Returns:
            ``S`` for ``SBuilder``.
        """

        x = self.x
        if isinstance(self.x, types.Real):
            x = self.x
        elif isinstance(self.x, float) or isinstance(self.x, int):
            x = types.Real(self.x)
        elif isinstance(self.x, str):
            x = types.Real.from_mcnp(self.x)

        y = self.y
        if isinstance(self.y, types.Real):
            y = self.y
        elif isinstance(self.y, float) or isinstance(self.y, int):
            y = types.Real(self.y)
        elif isinstance(self.y, str):
            y = types.Real.from_mcnp(self.y)

        z = self.z
        if isinstance(self.z, types.Real):
            z = self.z
        elif isinstance(self.z, float) or isinstance(self.z, int):
            z = types.Real(self.z)
        elif isinstance(self.z, str):
            z = types.Real.from_mcnp(self.z)

        r = self.r
        if isinstance(self.r, types.Real):
            r = self.r
        elif isinstance(self.r, float) or isinstance(self.r, int):
            r = types.Real(self.r)
        elif isinstance(self.r, str):
            r = types.Real.from_mcnp(self.r)

        return S(
            x=x,
            y=y,
            z=z,
            r=r,
        )

    @staticmethod
    def unbuild(ast: S):
        """
        Unbuilds ``S`` into ``SBuilder``

        Returns:
            ``SBuilder`` for ``S``.
        """

        return SBuilder(
            x=copy.deepcopy(ast.x),
            y=copy.deepcopy(ast.y),
            z=copy.deepcopy(ast.z),
            r=copy.deepcopy(ast.r),
        )
