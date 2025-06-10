import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Old(_option.SsrOption):
    """
    Represents INP old elements.

    Attributes:
        numbers: Tuple of surface numbers from subset of surfaces on SSW card.
    """

    _KEYWORD = 'old'

    _ATTRS = {
        'numbers': types.Tuple[types.Integer],
    }

    _REGEX = re.compile(rf'\Aold((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, numbers: types.Tuple[types.Integer]):
        """
        Initializes ``Old``.

        Parameters:
            numbers: Tuple of surface numbers from subset of surfaces on SSW card.

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
class OldBuilder(_option.SsrOptionBuilder):
    """
    Builds ``Old``.

    Attributes:
        numbers: Tuple of surface numbers from subset of surfaces on SSW card.
    """

    numbers: list[str] | list[int] | list[types.Integer]

    def build(self):
        """
        Builds ``OldBuilder`` into ``Old``.

        Returns:
            ``Old`` for ``OldBuilder``.
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

        return Old(
            numbers=numbers,
        )

    @staticmethod
    def unbuild(ast: Old):
        """
        Unbuilds ``Old`` into ``OldBuilder``

        Returns:
            ``OldBuilder`` for ``Old``.
        """

        return OldBuilder(
            numbers=copy.deepcopy(ast.numbers),
        )
