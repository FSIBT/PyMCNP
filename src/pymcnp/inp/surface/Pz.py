import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class Pz(_option.SurfaceOption):
    """
    Represents INP pz elements.

    Attributes:
        d: Normal-to-the-z-axis plane D coefficent.
    """

    _KEYWORD = 'pz'

    _ATTRS = {
        'd': types.Real,
    }

    _REGEX = re.compile(rf'\Apz( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, d: types.Real):
        """
        Initializes ``Pz``.

        Parameters:
            d: Normal-to-the-z-axis plane D coefficent.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if d is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, d)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                d,
            ]
        )

        self.d: typing.Final[types.Real] = d

    def draw(self):
        """
        Generates ``Visualization`` from ``Pz``.

        Returns:
            ``pyvista.PolyData`` for ``Pz``
        """

        vis = _visualization.Visualization.get_plane(0, 0, 1, float(self.d))

        return vis


@dataclasses.dataclass
class PzBuilder(_option.SurfaceOptionBuilder):
    """
    Builds ``Pz``.

    Attributes:
        d: Normal-to-the-z-axis plane D coefficent.
    """

    d: str | float | types.Real

    def build(self):
        """
        Builds ``PzBuilder`` into ``Pz``.

        Returns:
            ``Pz`` for ``PzBuilder``.
        """

        d = self.d
        if isinstance(self.d, types.Real):
            d = self.d
        elif isinstance(self.d, float) or isinstance(self.d, int):
            d = types.Real(self.d)
        elif isinstance(self.d, str):
            d = types.Real.from_mcnp(self.d)

        return Pz(
            d=d,
        )

    @staticmethod
    def unbuild(ast: Pz):
        """
        Unbuilds ``Pz`` into ``PzBuilder``

        Returns:
            ``PzBuilder`` for ``Pz``.
        """

        return PzBuilder(
            d=copy.deepcopy(ast.d),
        )
