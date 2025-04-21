import re
import typing
import dataclasses


from ._option import MeshOption
from ....utils import types
from ....utils import errors


class Kints(MeshOption, keyword='kints'):
    """
    Represents INP kints elements.

    Attributes:
        number: Number of fine meshes within corresponding coarse meshes in the z/theta directions.
    """

    _ATTRS = {
        'number': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Akints( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, number: types.IntegerOrJump):
        """
        Initializes ``Kints``.

        Parameters:
            number: Number of fine meshes within corresponding coarse meshes in the z/theta directions.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if number is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, number)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                number,
            ]
        )

        self.number: typing.Final[types.IntegerOrJump] = number


@dataclasses.dataclass
class KintsBuilder:
    """
    Builds ``Kints``.

    Attributes:
        number: Number of fine meshes within corresponding coarse meshes in the z/theta directions.
    """

    number: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``KintsBuilder`` into ``Kints``.

        Returns:
            ``Kints`` for ``KintsBuilder``.
        """

        if isinstance(self.number, types.Integer):
            number = self.number
        elif isinstance(self.number, int):
            number = types.IntegerOrJump(self.number)
        elif isinstance(self.number, str):
            number = types.IntegerOrJump.from_mcnp(self.number)

        return Kints(
            number=number,
        )
