import re
import copy
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

    _KEYWORD = 'fill'

    _ATTRS = {
        'numbers': types.Tuple[types.Integer],
    }

    _REGEX = re.compile(rf'\Afill((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, numbers: types.Tuple[types.Integer]):
        """
        Initializes ``Fill``.

        Parameters:
            numbers: Tuple of universe numbers.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if numbers is None or not (
            filter(lambda entry: not (0 <= entry.value <= 99_999_999), numbers)
        ):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, numbers)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                numbers,
            ]
        )

        self.numbers: typing.Final[types.Tuple[types.Integer]] = numbers


@dataclasses.dataclass
class FillBuilder:
    """
    Builds ``Fill``.

    Attributes:
        numbers: Tuple of universe numbers.
    """

    numbers: list[str] | list[int] | list[types.Integer]

    def build(self):
        """
        Builds ``FillBuilder`` into ``Fill``.

        Returns:
            ``Fill`` for ``FillBuilder``.
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

        return Fill(
            numbers=numbers,
        )

    @staticmethod
    def unbuild(ast: Fill):
        """
        Unbuilds ``Fill`` into ``FillBuilder``

        Returns:
            ``FillBuilder`` for ``Fill``.
        """

        return Fill(
            numbers=copy.deepcopy(ast.numbers),
        )
