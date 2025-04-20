import re
import typing
import dataclasses


from .option_ import KpertOption_
from ....utils import types
from ....utils import errors


class Cell(KpertOption_, keyword='cell'):
    """
    Represents INP cell elements.

    Attributes:
        numbers: List of cells.
    """

    _ATTRS = {
        'numbers': types.Tuple[types.IntegerOrJump],
    }

    _REGEX = re.compile(rf'\Acell((?: {types.IntegerOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, numbers: types.Tuple[types.IntegerOrJump]):
        """
        Initializes ``Cell``.

        Parameters:
            numbers: List of cells.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if numbers is None or not (filter(lambda entry: not (1 <= entry <= 99_999_999), numbers)):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, numbers)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                numbers,
            ]
        )

        self.numbers: typing.Final[types.Tuple[types.IntegerOrJump]] = numbers


@dataclasses.dataclass
class CellBuilder:
    """
    Builds ``Cell``.

    Attributes:
        numbers: List of cells.
    """

    numbers: list[str] | list[int] | list[types.IntegerOrJump]

    def build(self):
        """
        Builds ``CellBuilder`` into ``Cell``.

        Returns:
            ``Cell`` for ``CellBuilder``.
        """

        numbers = []
        for item in self.numbers:
            if isinstance(item, types.IntegerOrJump):
                numbers.append(item)
            elif isinstance(item, int):
                numbers.append(types.IntegerOrJump(item))
            elif isinstance(item, str):
                numbers.append(types.IntegerOrJump.from_mcnp(item))
        numbers = types.Tuple(numbers)

        return Cell(
            numbers=numbers,
        )
