import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Ffedges(_option.BfldOption):
    """
    Represents INP ffedges elements.

    Attributes:
        numbers: Surface numbers to apply field fringe edges.
    """

    _KEYWORD = 'ffedges'

    _ATTRS = {
        'numbers': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Affedges((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, numbers: types.Tuple[types.Real]):
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

        self.numbers: typing.Final[types.Tuple[types.Real]] = numbers


@dataclasses.dataclass
class FfedgesBuilder(_option.BfldOptionBuilder):
    """
    Builds ``Ffedges``.

    Attributes:
        numbers: Surface numbers to apply field fringe edges.
    """

    numbers: list[str] | list[float] | list[types.Real]

    def build(self):
        """
        Builds ``FfedgesBuilder`` into ``Ffedges``.

        Returns:
            ``Ffedges`` for ``FfedgesBuilder``.
        """

        if self.numbers:
            numbers = []
            for item in self.numbers:
                if isinstance(item, types.Real):
                    numbers.append(item)
                elif isinstance(item, float) or isinstance(item, int):
                    numbers.append(types.Real(item))
                elif isinstance(item, str):
                    numbers.append(types.Real.from_mcnp(item))
            numbers = types.Tuple(numbers)
        else:
            numbers = None

        return Ffedges(
            numbers=numbers,
        )

    @staticmethod
    def unbuild(ast: Ffedges):
        """
        Unbuilds ``Ffedges`` into ``FfedgesBuilder``

        Returns:
            ``FfedgesBuilder`` for ``Ffedges``.
        """

        return FfedgesBuilder(
            numbers=copy.deepcopy(ast.numbers),
        )
