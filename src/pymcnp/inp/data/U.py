import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class U(_option.DataOption):
    """
    Represents INP u elements.

    Attributes:
        numbers: Tuple of cell numbers.
    """

    _KEYWORD = 'u'

    _ATTRS = {
        'numbers': types.Tuple[types.Integer],
    }

    _REGEX = re.compile(rf'\Au((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, numbers: types.Tuple[types.Integer]):
        """
        Initializes ``U``.

        Parameters:
            numbers: Tuple of cell numbers.

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
class UBuilder(_option.DataOptionBuilder):
    """
    Builds ``U``.

    Attributes:
        numbers: Tuple of cell numbers.
    """

    numbers: list[str] | list[int] | list[types.Integer]

    def build(self):
        """
        Builds ``UBuilder`` into ``U``.

        Returns:
            ``U`` for ``UBuilder``.
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

        return U(
            numbers=numbers,
        )

    @staticmethod
    def unbuild(ast: U):
        """
        Unbuilds ``U`` into ``UBuilder``

        Returns:
            ``UBuilder`` for ``U``.
        """

        return UBuilder(
            numbers=copy.deepcopy(ast.numbers),
        )
