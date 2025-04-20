import re
import typing
import dataclasses


from .option_ import SurfaceOption_
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class Sx(SurfaceOption_, keyword='sx'):
    """
    Represents INP sx elements.

    Attributes:
        x: On-x-axis sphere center x component.
        r: On-x-axis sphere radius.
    """

    _ATTRS = {
        'x': types.Real,
        'r': types.Real,
    }

    _REGEX = re.compile(rf'\Asx( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})\Z')

    def __init__(self, x: types.Real, r: types.Real):
        """
        Initializes ``Sx``.

        Parameters:
            x: On-x-axis sphere center x component.
            r: On-x-axis sphere radius.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x)
        if r is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, r)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                x,
                r,
            ]
        )

        self.x: typing.Final[types.Real] = x
        self.r: typing.Final[types.Real] = r

    def draw(self):
        """
        Generates ``Visualization`` from ``Sx``.

        Returns:
            ``pyvista.PolyData`` for ``Sx``
        """

        vis = _visualization.Visualization.get_sphere(self.r.value)
        vis = vis.add_translation(_visualization.Vector(self.x.value, 0, 0))

        return vis


@dataclasses.dataclass
class SxBuilder:
    """
    Builds ``Sx``.

    Attributes:
        x: On-x-axis sphere center x component.
        r: On-x-axis sphere radius.
    """

    x: str | float | types.Real
    r: str | float | types.Real

    def build(self):
        """
        Builds ``SxBuilder`` into ``Sx``.

        Returns:
            ``Sx`` for ``SxBuilder``.
        """

        if isinstance(self.x, types.Real):
            x = self.x
        elif isinstance(self.x, float) or isinstance(self.x, int):
            x = types.Real(self.x)
        elif isinstance(self.x, str):
            x = types.Real.from_mcnp(self.x)

        if isinstance(self.r, types.Real):
            r = self.r
        elif isinstance(self.r, float) or isinstance(self.r, int):
            r = types.Real(self.r)
        elif isinstance(self.r, str):
            r = types.Real.from_mcnp(self.r)

        return Sx(
            x=x,
            r=r,
        )
