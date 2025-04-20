import re
import typing
import dataclasses


from .option_ import KpertOption_
from ....utils import types
from ....utils import errors


class Mat(KpertOption_, keyword='mat'):
    """
    Represents INP mat elements.

    Attributes:
        numbers: List of materials.
    """

    _ATTRS = {
        'numbers': types.Tuple[types.IntegerOrJump],
    }

    _REGEX = re.compile(rf'\Amat((?: {types.IntegerOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, numbers: types.Tuple[types.IntegerOrJump]):
        """
        Initializes ``Mat``.

        Parameters:
            numbers: List of materials.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if numbers is None or not (filter(lambda entry: not (0 <= entry <= 99_999_999), numbers)):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, numbers)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                numbers,
            ]
        )

        self.numbers: typing.Final[types.Tuple[types.IntegerOrJump]] = numbers


@dataclasses.dataclass
class MatBuilder:
    """
    Builds ``Mat``.

    Attributes:
        numbers: List of materials.
    """

    numbers: list[str] | list[int] | list[types.IntegerOrJump]

    def build(self):
        """
        Builds ``MatBuilder`` into ``Mat``.

        Returns:
            ``Mat`` for ``MatBuilder``.
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

        return Mat(
            numbers=numbers,
        )
