import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Z(_option.SdefOption):
    """
    Represents INP z elements.

    Attributes:
        z_coordinate: Z-cordinate of position.
    """

    _KEYWORD = 'z'

    _ATTRS = {
        'z_coordinate': types.Real,
    }

    _REGEX = re.compile(rf'\Az( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, z_coordinate: types.Real):
        """
        Initializes ``Z``.

        Parameters:
            z_coordinate: Z-cordinate of position.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if z_coordinate is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, z_coordinate)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                z_coordinate,
            ]
        )

        self.z_coordinate: typing.Final[types.Real] = z_coordinate


@dataclasses.dataclass
class ZBuilder(_option.SdefOptionBuilder):
    """
    Builds ``Z``.

    Attributes:
        z_coordinate: Z-cordinate of position.
    """

    z_coordinate: str | float | types.Real

    def build(self):
        """
        Builds ``ZBuilder`` into ``Z``.

        Returns:
            ``Z`` for ``ZBuilder``.
        """

        z_coordinate = self.z_coordinate
        if isinstance(self.z_coordinate, types.Real):
            z_coordinate = self.z_coordinate
        elif isinstance(self.z_coordinate, float) or isinstance(self.z_coordinate, int):
            z_coordinate = types.Real(self.z_coordinate)
        elif isinstance(self.z_coordinate, str):
            z_coordinate = types.Real.from_mcnp(self.z_coordinate)

        return Z(
            z_coordinate=z_coordinate,
        )

    @staticmethod
    def unbuild(ast: Z):
        """
        Unbuilds ``Z`` into ``ZBuilder``

        Returns:
            ``ZBuilder`` for ``Z``.
        """

        return ZBuilder(
            z_coordinate=copy.deepcopy(ast.z_coordinate),
        )
