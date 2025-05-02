import re
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

    _ATTRS = {
        'number': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Aiints( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, number: types.IntegerOrJump):
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

        self.number: typing.Final[types.IntegerOrJump] = number


@dataclasses.dataclass
class IintsBuilder:
    """
    Builds ``Iints``.

    Attributes:
        number: Number of fine meshes within corresponding coarse meshes in the x/r directions.
    """

    number: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``IintsBuilder`` into ``Iints``.

        Returns:
            ``Iints`` for ``IintsBuilder``.
        """

        if isinstance(self.number, types.Integer):
            number = self.number
        elif isinstance(self.number, int):
            number = types.IntegerOrJump(self.number)
        elif isinstance(self.number, str):
            number = types.IntegerOrJump.from_mcnp(self.number)

        return Iints(
            number=number,
        )
