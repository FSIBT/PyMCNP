import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Bflcl(_option.DataOption):
    """
    Represents INP bflcl elements.

    Attributes:
        numbers: Tuple of BFLD map numbers.
    """

    _KEYWORD = 'bflcl'

    _ATTRS = {
        'numbers': types.Tuple[types.Integer],
    }

    _REGEX = re.compile(rf'\Abflcl((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, numbers: types.Tuple[types.Integer]):
        """
        Initializes ``Bflcl``.

        Parameters:
            numbers: Tuple of BFLD map numbers.

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
class BflclBuilder(_option.DataOptionBuilder):
    """
    Builds ``Bflcl``.

    Attributes:
        numbers: Tuple of BFLD map numbers.
    """

    numbers: list[str] | list[int] | list[types.Integer]

    def build(self):
        """
        Builds ``BflclBuilder`` into ``Bflcl``.

        Returns:
            ``Bflcl`` for ``BflclBuilder``.
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

        return Bflcl(
            numbers=numbers,
        )

    @staticmethod
    def unbuild(ast: Bflcl):
        """
        Unbuilds ``Bflcl`` into ``BflclBuilder``

        Returns:
            ``BflclBuilder`` for ``Bflcl``.
        """

        return BflclBuilder(
            numbers=copy.deepcopy(ast.numbers),
        )
