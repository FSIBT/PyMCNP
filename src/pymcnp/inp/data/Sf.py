import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Sf(DataOption):
    """
    Represents INP sf elements.

    Attributes:
        suffix: Data card option suffix.
        numbers: Tallies for problem surface numbers to flag.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'numbers': types.Tuple[types.IntegerOrJump],
    }

    _REGEX = re.compile(rf'\Asf(\d+)((?: {types.IntegerOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, suffix: types.Integer, numbers: types.Tuple[types.IntegerOrJump]):
        """
        Initializes ``Sf``.

        Parameters:
            suffix: Data card option suffix.
            numbers: Tallies for problem surface numbers to flag.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if suffix is None or not (suffix <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)
        if numbers is None or not (filter(lambda entry: not (0 <= entry <= 99_999_999), numbers)):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, numbers)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                numbers,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.numbers: typing.Final[types.Tuple[types.IntegerOrJump]] = numbers


@dataclasses.dataclass
class SfBuilder:
    """
    Builds ``Sf``.

    Attributes:
        suffix: Data card option suffix.
        numbers: Tallies for problem surface numbers to flag.
    """

    suffix: str | int | types.Integer
    numbers: list[str] | list[int] | list[types.IntegerOrJump]

    def build(self):
        """
        Builds ``SfBuilder`` into ``Sf``.

        Returns:
            ``Sf`` for ``SfBuilder``.
        """

        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

        numbers = []
        for item in self.numbers:
            if isinstance(item, types.IntegerOrJump):
                numbers.append(item)
            elif isinstance(item, int):
                numbers.append(types.IntegerOrJump(item))
            elif isinstance(item, str):
                numbers.append(types.IntegerOrJump.from_mcnp(item))
        numbers = types.Tuple(numbers)

        return Sf(
            suffix=suffix,
            numbers=numbers,
        )
