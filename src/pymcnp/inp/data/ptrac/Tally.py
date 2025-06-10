import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Tally(_option.PtracOption):
    """
    Represents INP tally elements.

    Attributes:
        numbers: List of tally numbers for filtering.
    """

    _KEYWORD = 'tally'

    _ATTRS = {
        'numbers': types.Tuple[types.Integer],
    }

    _REGEX = re.compile(rf'\Atally((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, numbers: types.Tuple[types.Integer]):
        """
        Initializes ``Tally``.

        Parameters:
            numbers: List of tally numbers for filtering.

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
class TallyBuilder(_option.PtracOptionBuilder):
    """
    Builds ``Tally``.

    Attributes:
        numbers: List of tally numbers for filtering.
    """

    numbers: list[str] | list[int] | list[types.Integer]

    def build(self):
        """
        Builds ``TallyBuilder`` into ``Tally``.

        Returns:
            ``Tally`` for ``TallyBuilder``.
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

        return Tally(
            numbers=numbers,
        )

    @staticmethod
    def unbuild(ast: Tally):
        """
        Unbuilds ``Tally`` into ``TallyBuilder``

        Returns:
            ``TallyBuilder`` for ``Tally``.
        """

        return TallyBuilder(
            numbers=copy.deepcopy(ast.numbers),
        )
