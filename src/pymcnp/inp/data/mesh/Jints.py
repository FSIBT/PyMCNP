import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Jints(_option.MeshOption):
    """
    Represents INP jints elements.

    Attributes:
        number: Number of fine meshes within corresponding coarse meshes in the y/z directions.
    """

    _KEYWORD = 'jints'

    _ATTRS = {
        'number': types.Tuple[types.Integer],
    }

    _REGEX = re.compile(rf'\Ajints((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, number: types.Tuple[types.Integer]):
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

        self.number: typing.Final[types.Tuple[types.Integer]] = number


@dataclasses.dataclass
class JintsBuilder(_option.MeshOptionBuilder):
    """
    Builds ``Jints``.

    Attributes:
        number: Number of fine meshes within corresponding coarse meshes in the y/z directions.
    """

    number: list[str] | list[int] | list[types.Integer]

    def build(self):
        """
        Builds ``JintsBuilder`` into ``Jints``.

        Returns:
            ``Jints`` for ``JintsBuilder``.
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

        return Jints(
            number=number,
        )

    @staticmethod
    def unbuild(ast: Jints):
        """
        Unbuilds ``Jints`` into ``JintsBuilder``

        Returns:
            ``JintsBuilder`` for ``Jints``.
        """

        return JintsBuilder(
            number=copy.deepcopy(ast.number),
        )
