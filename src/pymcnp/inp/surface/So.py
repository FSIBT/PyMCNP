import re
import typing
import dataclasses


from ._option import SurfaceOption
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class So(SurfaceOption, keyword='so'):
    """
    Represents INP so elements.

    Attributes:
        r: Origin-centered sphere radius.
    """

    _ATTRS = {
        'r': types.Real,
    }

    _REGEX = re.compile(rf'\Aso( {types.Real._REGEX.pattern})\Z')

    def __init__(self, r: types.Real):
        """
        Initializes ``So``.

        Parameters:
            r: Origin-centered sphere radius.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if r is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, r)

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

        vis = _visualization.Visualization.get_sphere(self.r.value)

        return vis


@dataclasses.dataclass
class SoBuilder:
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

        if isinstance(self.r, types.Real):
            r = self.r
        elif isinstance(self.r, float) or isinstance(self.r, int):
            r = types.Real(self.r)
        elif isinstance(self.r, str):
            r = types.Real.from_mcnp(self.r)

        return So(
            r=r,
        )
