import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Mat(_option.KpertOption):
    """
    Represents INP mat elements.

    Attributes:
        numbers: List of materials.
    """

    _KEYWORD = 'mat'

    _ATTRS = {
        'numbers': types.Tuple[types.Integer],
    }

    _REGEX = re.compile(rf'\Amat((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, numbers: types.Tuple[types.Integer]):
        """
        Initializes ``Mat``.

        Parameters:
            numbers: List of materials.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if numbers is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, numbers)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                numbers,
            ]
        )

        self.numbers: typing.Final[types.Tuple[types.Integer]] = numbers


@dataclasses.dataclass
class MatBuilder(_option.KpertOptionBuilder):
    """
    Builds ``Mat``.

    Attributes:
        numbers: List of materials.
    """

    numbers: list[str] | list[int] | list[types.Integer]

    def build(self):
        """
        Builds ``MatBuilder`` into ``Mat``.

        Returns:
            ``Mat`` for ``MatBuilder``.
        """

        if self.numbers:
            numbers = []
            for item in self.numbers:
                if isinstance(item, types.Integer):
                    numbers.append(item)
                elif isinstance(item, int):
                    numbers.append(types.Integer(item))
                elif isinstance(item, str):
                    numbers.append(types.Integer.from_mcnp(item))
            numbers = types.Tuple(numbers)
        else:
            numbers = None

        return Mat(
            numbers=numbers,
        )

    @staticmethod
    def unbuild(ast: Mat):
        """
        Unbuilds ``Mat`` into ``MatBuilder``

        Returns:
            ``MatBuilder`` for ``Mat``.
        """

        return MatBuilder(
            numbers=copy.deepcopy(ast.numbers),
        )
