import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Fill(DataOption):
    """
    Represents INP fill elements.

    Attributes:
        numbers: Tuple of universe numbers.
    """

    _ATTRS = {
        'numbers': types.Tuple[types.IntegerOrJump],
    }

    _REGEX = re.compile(rf'\Afill((?: {types.IntegerOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, numbers: types.Tuple[types.IntegerOrJump]):
        """
        Initializes ``Fill``.

        Parameters:
            numbers: Tuple of universe numbers.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if numbers is None or not (filter(lambda entry: not (0 <= entry <= 99_999_999), numbers)):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, numbers)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                numbers,
            ]
        )

        self.numbers: typing.Final[types.Tuple[types.IntegerOrJump]] = numbers


@dataclasses.dataclass
class FillBuilder:
    """
    Builds ``Fill``.

    Attributes:
        numbers: Tuple of universe numbers.
    """

    numbers: list[str] | list[int] | list[types.IntegerOrJump]

    def build(self):
        """
        Builds ``FillBuilder`` into ``Fill``.

        Returns:
            ``Fill`` for ``FillBuilder``.
        """

        if self.numbers:
            numbers = []
            for item in self.numbers:
                if isinstance(item, types.IntegerOrJump):
                    numbers.append(item)
                elif isinstance(item, int):
                    numbers.append(types.IntegerOrJump(item))
                elif isinstance(item, str):
                    numbers.append(types.IntegerOrJump.from_mcnp(item))
            numbers = types.Tuple(numbers)
        else:
            numbers = None

        return Fill(
            numbers=numbers,
        )
