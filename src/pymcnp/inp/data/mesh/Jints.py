import re
import typing
import dataclasses


from ._option import MeshOption
from ....utils import types
from ....utils import errors


class Jints(MeshOption):
    """
    Represents INP jints elements.

    Attributes:
        number: Number of fine meshes within corresponding coarse meshes in the y/z directions.
    """

    _ATTRS = {
        'number': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Ajints( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, number: types.IntegerOrJump):
        """
        Initializes ``Jints``.

        Parameters:
            number: Number of fine meshes within corresponding coarse meshes in the y/z directions.

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
class JintsBuilder:
    """
    Builds ``Jints``.

    Attributes:
        number: Number of fine meshes within corresponding coarse meshes in the y/z directions.
    """

    number: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``JintsBuilder`` into ``Jints``.

        Returns:
            ``Jints`` for ``JintsBuilder``.
        """

        number = self.number
        if isinstance(self.number, types.Integer):
            number = self.number
        elif isinstance(self.number, int):
            number = types.IntegerOrJump(self.number)
        elif isinstance(self.number, str):
            number = types.IntegerOrJump.from_mcnp(self.number)

        return Jints(
            number=number,
        )
