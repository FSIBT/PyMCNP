import re
import copy
import typing
import dataclasses


from ._option import SurfaceOption
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class Sy(SurfaceOption):
    """
    Represents INP sy elements.

    Attributes:
        y: On-y-axis sphere center y component.
        r: On-y-axis sphere radius.
    """

    _KEYWORD = 'sy'

    _ATTRS = {
        'y': types.Real,
        'r': types.Real,
    }

    _REGEX = re.compile(
        rf'\Asy( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z'
    )

    def __init__(self, y: types.Real, r: types.Real):
        """
        Initializes ``Sy``.

        Parameters:
            y: On-y-axis sphere center y component.
            r: On-y-axis sphere radius.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if y is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, y)
        if r is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, r)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                y,
                r,
            ]
        )

        self.y: typing.Final[types.Real] = y
        self.r: typing.Final[types.Real] = r

    def draw(self):
        """
        Generates ``Visualization`` from ``Sy``.

        Returns:
            ``pyvista.PolyData`` for ``Sy``
        """

        vis = _visualization.Visualization.get_sphere(self.r.value)
        vis = vis.add_rotation(_visualization.Vector(1, 0, 0), 90, (0, 0, 0))
        vis = vis.add_translation(_visualization.Vector(0, self.y.value, 0))

        return vis


@dataclasses.dataclass
class SyBuilder:
    """
    Builds ``Sy``.

    Attributes:
        y: On-y-axis sphere center y component.
        r: On-y-axis sphere radius.
    """

    y: str | float | types.Real
    r: str | float | types.Real

    def build(self):
        """
        Builds ``SyBuilder`` into ``Sy``.

        Returns:
            ``Sy`` for ``SyBuilder``.
        """

        y = self.y
        if isinstance(self.y, types.Real):
            y = self.y
        elif isinstance(self.y, float) or isinstance(self.y, int):
            y = types.Real(self.y)
        elif isinstance(self.y, str):
            y = types.Real.from_mcnp(self.y)

        r = self.r
        if isinstance(self.r, types.Real):
            r = self.r
        elif isinstance(self.r, float) or isinstance(self.r, int):
            r = types.Real(self.r)
        elif isinstance(self.r, str):
            r = types.Real.from_mcnp(self.r)

        return Sy(
            y=y,
            r=r,
        )

    @staticmethod
    def unbuild(ast: Sy):
        """
        Unbuilds ``Sy`` into ``SyBuilder``

        Returns:
            ``SyBuilder`` for ``Sy``.
        """

        return Sy(
            y=copy.deepcopy(ast.y),
            r=copy.deepcopy(ast.r),
        )
