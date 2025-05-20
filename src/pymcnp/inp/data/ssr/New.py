import re
import typing
import dataclasses


from ._option import SsrOption
from ....utils import types
from ....utils import errors


class New(SsrOption):
    """
    Represents INP new elements.

    Attributes:
        numbers: Tuple of surface numbers to start run.
    """

    _ATTRS = {
        'numbers': types.Tuple[types.Integer],
    }

    _REGEX = re.compile(rf'\Anew((?: {types.Integer._REGEX.pattern})+?)\Z')

    def __init__(self, numbers: types.Tuple[types.Integer]):
        """
        Initializes ``New``.

        Parameters:
            numbers: Tuple of surface numbers to start run.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if numbers is None or not (
            filter(lambda entry: not (1 <= entry.value <= 99_999_999), numbers)
        ):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, numbers)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                numbers,
            ]
        )

        self.numbers: typing.Final[types.Tuple[types.Integer]] = numbers


@dataclasses.dataclass
class NewBuilder:
    """
    Builds ``New``.

    Attributes:
        numbers: Tuple of surface numbers to start run.
    """

    numbers: list[str] | list[int] | list[types.Integer]

    def build(self):
        """
        Builds ``NewBuilder`` into ``New``.

        Returns:
            ``New`` for ``NewBuilder``.
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

        return New(
            numbers=numbers,
        )
