import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Cosy(DataOption):
    """
    Represents INP cosy elements.

    Attributes:
        numbers: Tuple of COSY map numbers.
    """

    _ATTRS = {
        'numbers': types.Tuple[types.IntegerOrJump],
    }

    _REGEX = re.compile(rf'\Acosy((?: {types.IntegerOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, numbers: types.Tuple[types.IntegerOrJump]):
        """
        Initializes ``Cosy``.

        Parameters:
            numbers: Tuple of COSY map numbers.

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

        self.numbers: typing.Final[types.Tuple[types.IntegerOrJump]] = numbers


@dataclasses.dataclass
class CosyBuilder:
    """
    Builds ``Cosy``.

    Attributes:
        numbers: Tuple of COSY map numbers.
    """

    numbers: list[str] | list[int] | list[types.IntegerOrJump]

    def build(self):
        """
        Builds ``CosyBuilder`` into ``Cosy``.

        Returns:
            ``Cosy`` for ``CosyBuilder``.
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

        return Cosy(
            numbers=numbers,
        )
