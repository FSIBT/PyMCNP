import re
import typing
import dataclasses


from ._option import MeshOption
from ....utils import types
from ....utils import errors


class Kints(MeshOption):
    """
    Represents INP kints elements.

    Attributes:
        number: Number of fine meshes within corresponding coarse meshes in the z/theta directions.
    """

    _ATTRS = {
        'number': types.Integer,
    }

    _REGEX = re.compile(rf'\Akints( {types.Integer._REGEX.pattern})\Z')

    def __init__(self, number: types.Integer):
        """
        Initializes ``Kints``.

        Parameters:
            number: Number of fine meshes within corresponding coarse meshes in the z/theta directions.

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
class KintsBuilder:
    """
    Builds ``Kints``.

    Attributes:
        number: Number of fine meshes within corresponding coarse meshes in the z/theta directions.
    """

    number: str | int | types.Integer

    def build(self):
        """
        Builds ``KintsBuilder`` into ``Kints``.

        Returns:
            ``Kints`` for ``KintsBuilder``.
        """

        number = self.number
        if isinstance(self.number, types.Integer):
            number = self.number
        elif isinstance(self.number, int):
            number = types.Integer(self.number)
        elif isinstance(self.number, str):
            number = types.Integer.from_mcnp(self.number)

        return Kints(
            number=number,
        )
