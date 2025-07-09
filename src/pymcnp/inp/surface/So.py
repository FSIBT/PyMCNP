import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class So(_option.SurfaceOption):
    """
    Represents INP so elements.

    Attributes:
        r: Origin-centered sphere radius.
    """

    _KEYWORD = 'so'

    _ATTRS = {
        'r': types.Real,
    }

    _REGEX = re.compile(rf'\Aso( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, r: types.Real):
        """
        Initializes ``So``.

        Parameters:
            r: Origin-centered sphere radius.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if r is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, r)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                r,
            ]
        )

        self.r: typing.Final[types.Real] = r

    def draw(self):
        """
        Generates ``Visualization`` from ``So``.

        Returns:
            ``pyvista.PolyData`` for ``So``
        """

        vis = _visualization.Visualization.get_sphere(float(self.r))

        return vis


@dataclasses.dataclass
class SoBuilder(_option.SurfaceOptionBuilder):
    """
    Builds ``So``.

    Attributes:
        r: Origin-centered sphere radius.
    """

    r: str | float | types.Real

    def build(self):
        """
        Builds ``SoBuilder`` into ``So``.

        Returns:
            ``So`` for ``SoBuilder``.
        """

        r = self.r
        if isinstance(self.r, types.Real):
            r = self.r
        elif isinstance(self.r, float) or isinstance(self.r, int):
            r = types.Real(self.r)
        elif isinstance(self.r, str):
            r = types.Real.from_mcnp(self.r)

        return So(
            r=r,
        )

    @staticmethod
    def unbuild(ast: So):
        """
        Unbuilds ``So`` into ``SoBuilder``

        Returns:
            ``SoBuilder`` for ``So``.
        """

        return SoBuilder(
            r=copy.deepcopy(ast.r),
        )
