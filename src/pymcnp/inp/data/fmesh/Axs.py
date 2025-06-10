import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Axs(_option.FmeshOption):
    """
    Represents INP axs elements.

    Attributes:
        x: Cylindrical mesh axis vector x component.
        y: Cylindrical mesh axis vector y component.
        z: Cylindrical mesh axis vector z component.
    """

    _KEYWORD = 'axs'

    _ATTRS = {
        'x': types.Real,
        'y': types.Real,
        'z': types.Real,
    }

    _REGEX = re.compile(rf'\Aaxs( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, x: types.Real, y: types.Real, z: types.Real):
        """
        Initializes ``Axs``.

        Parameters:
            x: Cylindrical mesh axis vector x component.
            y: Cylindrical mesh axis vector y component.
            z: Cylindrical mesh axis vector z component.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x)
        if y is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, y)
        if z is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, z)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                x,
                y,
                z,
            ]
        )

        self.x: typing.Final[types.Real] = x
        self.y: typing.Final[types.Real] = y
        self.z: typing.Final[types.Real] = z


@dataclasses.dataclass
class AxsBuilder(_option.FmeshOptionBuilder):
    """
    Builds ``Axs``.

    Attributes:
        x: Cylindrical mesh axis vector x component.
        y: Cylindrical mesh axis vector y component.
        z: Cylindrical mesh axis vector z component.
    """

    x: str | float | types.Real
    y: str | float | types.Real
    z: str | float | types.Real

    def build(self):
        """
        Builds ``AxsBuilder`` into ``Axs``.

        Returns:
            ``Axs`` for ``AxsBuilder``.
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

        return Axs(
            x=x,
            y=y,
            z=z,
        )

    @staticmethod
    def unbuild(ast: Axs):
        """
        Unbuilds ``Axs`` into ``AxsBuilder``

        Returns:
            ``AxsBuilder`` for ``Axs``.
        """

        return AxsBuilder(
            x=copy.deepcopy(ast.x),
            y=copy.deepcopy(ast.y),
            z=copy.deepcopy(ast.z),
        )
