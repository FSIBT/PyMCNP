import re
import copy
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

    _KEYWORD = 'kints'

    _ATTRS = {
        'number': types.Tuple[types.Integer],
    }

    _REGEX = re.compile(rf'\Akints((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, number: types.Tuple[types.Integer]):
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

        self.number: typing.Final[types.Tuple[types.Integer]] = number


@dataclasses.dataclass
class KintsBuilder:
    """
    Builds ``Kints``.

    Attributes:
        number: Number of fine meshes within corresponding coarse meshes in the z/theta directions.
    """

    number: list[str] | list[int] | list[types.Integer]

    def build(self):
        """
        Builds ``KintsBuilder`` into ``Kints``.

        Returns:
            ``Kints`` for ``KintsBuilder``.
        """

        if self.number:
            number = []
            for item in self.number:
                if isinstance(item, types.Integer):
                    number.append(item)
                elif isinstance(item, int):
                    number.append(types.Integer(item))
                elif isinstance(item, str):
                    number.append(types.Integer.from_mcnp(item))
            number = types.Tuple(number)
        else:
            number = None

        return Kints(
            number=number,
        )

    @staticmethod
    def unbuild(ast: Kints):
        """
        Unbuilds ``Kints`` into ``KintsBuilder``

        Returns:
            ``KintsBuilder`` for ``Kints``.
        """

        return Kints(
            number=copy.deepcopy(ast.number),
        )
