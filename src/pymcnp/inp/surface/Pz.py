import re
import typing
import dataclasses


from .option_ import SurfaceOption_
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class Pz(SurfaceOption_, keyword='pz'):
    """
    Represents INP pz elements.

    Attributes:
        d: Normal-to-the-z-axis plane D coefficent.
    """

    _ATTRS = {
        'd': types.Real,
    }

    _REGEX = re.compile(rf'\Apz( {types.Real._REGEX.pattern})\Z')

    def __init__(self, d: types.Real):
        """
        Initializes ``Pz``.

        Parameters:
            d: Normal-to-the-z-axis plane D coefficent.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if d is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, d)

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

        vis = _visualization.Visualization.get_plane(0, 0, 1, self.d.value)

        return vis


@dataclasses.dataclass
class PzBuilder:
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

        if isinstance(self.d, types.Real):
            d = self.d
        elif isinstance(self.d, float) or isinstance(self.d, int):
            d = types.Real(self.d)
        elif isinstance(self.d, str):
            d = types.Real.from_mcnp(self.d)

        return Pz(
            d=d,
        )
