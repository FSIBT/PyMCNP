import re
import copy
import typing
import dataclasses


from ._option import SurfaceOption
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class Py(SurfaceOption):
    """
    Represents INP py elements.

    Attributes:
        d: Normal-to-the-y-axis plane D coefficent.
    """

    _KEYWORD = 'py'

    _ATTRS = {
        'd': types.Real,
    }

    _REGEX = re.compile(rf'\Apy( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, d: types.Real):
        """
        Initializes ``Py``.

        Parameters:
            d: Normal-to-the-y-axis plane D coefficent.

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
        Generates ``Visualization`` from ``Py``.

        Returns:
            ``pyvista.PolyData`` for ``Py``
        """

        vis = _visualization.Visualization.get_plane(0, 1, 0, self.d.value)
        vis = vis.add_rotation(_visualization.Vector(1, 0, 0), 90, (0, 0, 0))

        return vis


@dataclasses.dataclass
class PyBuilder:
    """
    Builds ``Py``.

    Attributes:
        d: Normal-to-the-y-axis plane D coefficent.
    """

    d: str | float | types.Real

    def build(self):
        """
        Builds ``PyBuilder`` into ``Py``.

        Returns:
            ``Py`` for ``PyBuilder``.
        """

        d = self.d
        if isinstance(self.d, types.Real):
            d = self.d
        elif isinstance(self.d, float) or isinstance(self.d, int):
            d = types.Real(self.d)
        elif isinstance(self.d, str):
            d = types.Real.from_mcnp(self.d)

        return Py(
            d=d,
        )

    @staticmethod
    def unbuild(ast: Py):
        """
        Unbuilds ``Py`` into ``PyBuilder``

        Returns:
            ``PyBuilder`` for ``Py``.
        """

        return Py(
            d=copy.deepcopy(ast.d),
        )
