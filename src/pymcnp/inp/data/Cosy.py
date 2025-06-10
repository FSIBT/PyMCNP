import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Cosy(_option.DataOption):
    """
    Represents INP cosy elements.

    Attributes:
        numbers: Tuple of COSY map numbers.
    """

    _KEYWORD = 'cosy'

    _ATTRS = {
        'numbers': types.Tuple[types.Integer],
    }

    _REGEX = re.compile(rf'\Acosy((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, numbers: types.Tuple[types.Integer]):
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

        self.numbers: typing.Final[types.Tuple[types.Integer]] = numbers


@dataclasses.dataclass
class CosyBuilder(_option.DataOptionBuilder):
    """
    Builds ``Cosy``.

    Attributes:
        numbers: Tuple of COSY map numbers.
    """

    numbers: list[str] | list[int] | list[types.Integer]

    def build(self):
        """
        Builds ``CosyBuilder`` into ``Cosy``.

        Returns:
            ``Cosy`` for ``CosyBuilder``.
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

        return Cosy(
            numbers=numbers,
        )

    @staticmethod
    def unbuild(ast: Cosy):
        """
        Unbuilds ``Cosy`` into ``CosyBuilder``

        Returns:
            ``CosyBuilder`` for ``Cosy``.
        """

        return CosyBuilder(
            numbers=copy.deepcopy(ast.numbers),
        )
