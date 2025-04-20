import re
import typing
import dataclasses


from .option_ import SurfaceOption_
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class Cz(SurfaceOption_, keyword='cz'):
    """
    Represents INP cz elements.

    Attributes:
        r: On-z-axis cylinder radius.
    """

    _ATTRS = {
        'r': types.Real,
    }

    _REGEX = re.compile(rf'\Acz( {types.Real._REGEX.pattern})\Z')

    def __init__(self, r: types.Real):
        """
        Initializes ``Cz``.

        Parameters:
            r: On-z-axis cylinder radius.

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
        Generates ``Visualization`` from ``Cz``.

        Returns:
            ``pyvista.PolyData`` for ``Cz``.
        """

        vis = _visualization.Visualization.get_cylinder_unbounded(self.r.value)

        return vis


@dataclasses.dataclass
class CzBuilder:
    """
    Builds ``Cz``.

    Attributes:
        r: On-z-axis cylinder radius.
    """

    r: str | float | types.Real

    def build(self):
        """
        Builds ``CzBuilder`` into ``Cz``.

        Returns:
            ``Cz`` for ``CzBuilder``.
        """

        if isinstance(self.r, types.Real):
            r = self.r
        elif isinstance(self.r, float) or isinstance(self.r, int):
            r = types.Real(self.r)
        elif isinstance(self.r, str):
            r = types.Real.from_mcnp(self.r)

        return Cz(
            r=r,
        )
