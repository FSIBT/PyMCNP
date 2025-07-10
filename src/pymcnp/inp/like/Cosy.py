import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Cosy(_option.LikeOption):
    """
    Represents INP cosy elements.

    Attributes:
        number: Like cosy map number.
    """

    _KEYWORD = 'cosy'

    _ATTRS = {
        'number': types.Integer,
    }

    _REGEX = re.compile(rf'\Acosy( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, number: types.Integer):
        """
        Initializes ``Cosy``.

        Parameters:
            number: Like cosy map number.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if number is None or number not in {1, 2, 3, 4, 5, 6}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, number)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                number,
            ]
        )

        self.number: typing.Final[types.Integer] = number


@dataclasses.dataclass
class CosyBuilder(_option.LikeOptionBuilder):
    """
    Builds ``Cosy``.

    Attributes:
        number: Like cosy map number.
    """

    number: str | int | types.Integer

    def build(self):
        """
        Builds ``CosyBuilder`` into ``Cosy``.

        Returns:
            ``Cosy`` for ``CosyBuilder``.
        """

        number = self.number
        if isinstance(self.number, types.Integer):
            number = self.number
        elif isinstance(self.number, int):
            number = types.Integer(self.number)
        elif isinstance(self.number, str):
            number = types.Integer.from_mcnp(self.number)

        return Cosy(
            number=number,
        )

    @staticmethod
    def unbuild(ast: Cosy):
        """
        Unbuilds ``Cosy`` into ``CosyBuilder``

        Returns:
            ``CosyBuilder`` for ``Cosy``.
        """

        return CosyBuilder(
            number=copy.deepcopy(ast.number),
        )
