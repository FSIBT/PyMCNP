import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Cell(_option.KpertOption):
    """
    Represents INP cell elements.

    Attributes:
        numbers: List of cells.
    """

    _KEYWORD = 'cell'

    _ATTRS = {
        'numbers': types.Tuple[types.Integer],
    }

    _REGEX = re.compile(rf'\Acell((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, numbers: types.Tuple[types.Integer]):
        """
        Initializes ``Cell``.

        Parameters:
            numbers: List of cells.

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
class CellBuilder(_option.KpertOptionBuilder):
    """
    Builds ``Cell``.

    Attributes:
        numbers: List of cells.
    """

    numbers: list[str] | list[int] | list[types.Integer]

    def build(self):
        """
        Builds ``CellBuilder`` into ``Cell``.

        Returns:
            ``Cell`` for ``CellBuilder``.
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

        return Cell(
            numbers=numbers,
        )

    @staticmethod
    def unbuild(ast: Cell):
        """
        Unbuilds ``Cell`` into ``CellBuilder``

        Returns:
            ``CellBuilder`` for ``Cell``.
        """

        return CellBuilder(
            numbers=copy.deepcopy(ast.numbers),
        )
