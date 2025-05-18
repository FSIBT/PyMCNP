import re
import typing
import dataclasses


from ._option import BfldOption
from ....utils import types
from ....utils import errors


class Ffedges(BfldOption):
    """
    Represents INP ffedges elements.

    Attributes:
        numbers: Surface numbers to apply field fringe edges.
    """

    _ATTRS = {
        'numbers': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(rf'\Affedges((?: {types.RealOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, numbers: types.Tuple[types.RealOrJump]):
        """
        Initializes ``Ffedges``.

        Parameters:
            numbers: Surface numbers to apply field fringe edges.

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

        self.numbers: typing.Final[types.Tuple[types.RealOrJump]] = numbers


@dataclasses.dataclass
class FfedgesBuilder:
    """
    Builds ``Ffedges``.

    Attributes:
        numbers: Surface numbers to apply field fringe edges.
    """

    numbers: list[str] | list[float] | list[types.RealOrJump]

    def build(self):
        """
        Builds ``FfedgesBuilder`` into ``Ffedges``.

        Returns:
            ``Ffedges`` for ``FfedgesBuilder``.
        """

        if self.numbers:
            numbers = []
            for item in self.numbers:
                if isinstance(item, types.RealOrJump):
                    numbers.append(item)
                elif isinstance(item, float) or isinstance(item, int):
                    numbers.append(types.RealOrJump(item))
                elif isinstance(item, str):
                    numbers.append(types.RealOrJump.from_mcnp(item))
            numbers = types.Tuple(numbers)
        else:
            numbers = None

        return Ffedges(
            numbers=numbers,
        )
