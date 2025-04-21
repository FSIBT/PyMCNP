import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Bflcl(DataOption, keyword='bflcl'):
    """
    Represents INP bflcl elements.

    Attributes:
        numbers: Tuple of BFLD map numbers.
    """

    _ATTRS = {
        'numbers': types.Tuple[types.IntegerOrJump],
    }

    _REGEX = re.compile(rf'\Abflcl((?: {types.IntegerOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, numbers: types.Tuple[types.IntegerOrJump]):
        """
        Initializes ``Bflcl``.

        Parameters:
            numbers: Tuple of BFLD map numbers.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if numbers is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, numbers)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                numbers,
            ]
        )

        self.numbers: typing.Final[types.Tuple[types.IntegerOrJump]] = numbers


@dataclasses.dataclass
class BflclBuilder:
    """
    Builds ``Bflcl``.

    Attributes:
        numbers: Tuple of BFLD map numbers.
    """

    numbers: list[str] | list[int] | list[types.IntegerOrJump]

    def build(self):
        """
        Builds ``BflclBuilder`` into ``Bflcl``.

        Returns:
            ``Bflcl`` for ``BflclBuilder``.
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

        return Bflcl(
            numbers=numbers,
        )
