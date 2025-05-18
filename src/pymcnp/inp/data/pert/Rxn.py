import re
import typing
import dataclasses


from ._option import PertOption
from ....utils import types
from ....utils import errors


class Rxn(PertOption):
    """
    Represents INP rxn elements.

    Attributes:
        numbers: ENDF/B reaction number.
    """

    _ATTRS = {
        'numbers': types.Tuple[types.IntegerOrJump],
    }

    _REGEX = re.compile(rf'\Arxn((?: {types.IntegerOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, numbers: types.Tuple[types.IntegerOrJump]):
        """
        Initializes ``Rxn``.

        Parameters:
            numbers: ENDF/B reaction number.

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
class RxnBuilder:
    """
    Builds ``Rxn``.

    Attributes:
        numbers: ENDF/B reaction number.
    """

    numbers: list[str] | list[int] | list[types.IntegerOrJump]

    def build(self):
        """
        Builds ``RxnBuilder`` into ``Rxn``.

        Returns:
            ``Rxn`` for ``RxnBuilder``.
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

        return Rxn(
            numbers=numbers,
        )
