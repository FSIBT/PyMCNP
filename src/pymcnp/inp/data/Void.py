import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Void(DataOption):
    """
    Represents INP void elements.

    Attributes:
        numbers: Tuple of cell numbers.
    """

    _ATTRS = {
        'numbers': types.Tuple[types.IntegerOrJump],
    }

    _REGEX = re.compile(rf'\Avoid((?: {types.IntegerOrJump._REGEX.pattern})+?)?\Z')

    def __init__(self, numbers: types.Tuple[types.IntegerOrJump] = None):
        """
        Initializes ``Void``.

        Parameters:
            numbers: Tuple of cell numbers.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if numbers is not None and not (
            filter(lambda entry: not (1 <= entry <= 99_999_999), numbers)
        ):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, numbers)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                numbers,
            ]
        )

        self.numbers: typing.Final[types.Tuple[types.IntegerOrJump]] = numbers


@dataclasses.dataclass
class VoidBuilder:
    """
    Builds ``Void``.

    Attributes:
        numbers: Tuple of cell numbers.
    """

    numbers: list[str] | list[int] | list[types.IntegerOrJump] = None

    def build(self):
        """
        Builds ``VoidBuilder`` into ``Void``.

        Returns:
            ``Void`` for ``VoidBuilder``.
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

        return Void(
            numbers=numbers,
        )
