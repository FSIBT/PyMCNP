import re
import copy
import typing
import dataclasses


from ._option import MeshOption
from ....utils import types
from ....utils import errors


class Iints(MeshOption):
    """
    Represents INP iints elements.

    Attributes:
        number: Number of fine meshes within corresponding coarse meshes in the x/r directions.
    """

    _KEYWORD = 'iints'

    _ATTRS = {
        'number': types.Integer,
    }

    _REGEX = re.compile(rf'\Aiints( {types.Integer._REGEX.pattern})\Z')

    def __init__(self, number: types.Integer):
        """
        Initializes ``Iints``.

        Parameters:
            number: Number of fine meshes within corresponding coarse meshes in the x/r directions.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if number is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, number)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                number,
            ]
        )

        self.number: typing.Final[types.Integer] = number


@dataclasses.dataclass
class IintsBuilder:
    """
    Builds ``Iints``.

    Attributes:
        number: Number of fine meshes within corresponding coarse meshes in the x/r directions.
    """

    number: str | int | types.Integer

    def build(self):
        """
        Builds ``IintsBuilder`` into ``Iints``.

        Returns:
            ``Iints`` for ``IintsBuilder``.
        """

        number = self.number
        if isinstance(self.number, types.Integer):
            number = self.number
        elif isinstance(self.number, int):
            number = types.Integer(self.number)
        elif isinstance(self.number, str):
            number = types.Integer.from_mcnp(self.number)

        return Iints(
            number=number,
        )

    @staticmethod
    def unbuild(ast: Iints):
        """
        Unbuilds ``Iints`` into ``IintsBuilder``

        Returns:
            ``IintsBuilder`` for ``Iints``.
        """

        return Iints(
            number=copy.deepcopy(ast.number),
        )
