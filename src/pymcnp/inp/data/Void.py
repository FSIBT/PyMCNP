import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types


class Void(_option.DataOption):
    """
    Represents INP void elements.

    Attributes:
        numbers: Tuple of cell numbers.
    """

    _KEYWORD = 'void'

    _ATTRS = {
        'numbers': types.Tuple[types.Integer],
    }

    _REGEX = re.compile(rf'\Avoid((?: {types.Integer._REGEX.pattern[2:-2]})+?)?\Z')

    def __init__(self, numbers: types.Tuple[types.Integer] = None):
        """
        Initializes ``Void``.

        Parameters:
            numbers: Tuple of cell numbers.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                numbers,
            ]
        )

        self.numbers: typing.Final[types.Tuple[types.Integer]] = numbers


@dataclasses.dataclass
class VoidBuilder(_option.DataOptionBuilder):
    """
    Builds ``Void``.

    Attributes:
        numbers: Tuple of cell numbers.
    """

    numbers: list[str] | list[int] | list[types.Integer] = None

    def build(self):
        """
        Builds ``VoidBuilder`` into ``Void``.

        Returns:
            ``Void`` for ``VoidBuilder``.
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

        return Void(
            numbers=numbers,
        )

    @staticmethod
    def unbuild(ast: Void):
        """
        Unbuilds ``Void`` into ``VoidBuilder``

        Returns:
            ``VoidBuilder`` for ``Void``.
        """

        return VoidBuilder(
            numbers=copy.deepcopy(ast.numbers),
        )
