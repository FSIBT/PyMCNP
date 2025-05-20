import re
import typing
import dataclasses


from ._option import KsenOption
from ....utils import types
from ....utils import errors


class Mt(KsenOption):
    """
    Represents INP mt elements.

    Attributes:
        numbers: List of reaction numbers for pertubation.
    """

    _ATTRS = {
        'numbers': types.Tuple[types.Integer],
    }

    _REGEX = re.compile(rf'\Amt((?: {types.Integer._REGEX.pattern})+?)\Z')

    def __init__(self, numbers: types.Tuple[types.Integer]):
        """
        Initializes ``Mt``.

        Parameters:
            numbers: List of reaction numbers for pertubation.

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
class MtBuilder:
    """
    Builds ``Mt``.

    Attributes:
        numbers: List of reaction numbers for pertubation.
    """

    numbers: list[str] | list[int] | list[types.Integer]

    def build(self):
        """
        Builds ``MtBuilder`` into ``Mt``.

        Returns:
            ``Mt`` for ``MtBuilder``.
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

        return Mt(
            numbers=numbers,
        )
