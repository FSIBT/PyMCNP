import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class U(_option.CellOption):
    """
    Represents INP u elements.

    Attributes:
        number: Cell universe number.
    """

    _KEYWORD = 'u'

    _ATTRS = {
        'number': types.Integer,
    }

    _REGEX = re.compile(rf'\Au( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, number: types.Integer):
        """
        Initializes ``U``.

        Parameters:
            number: Cell universe number.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if number is None or not (-99_999_999 <= number.value <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, number)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                number,
            ]
        )

        self.number: typing.Final[types.Integer] = number


@dataclasses.dataclass
class UBuilder(_option.CellOptionBuilder):
    """
    Builds ``U``.

    Attributes:
        number: Cell universe number.
    """

    number: str | int | types.Integer

    def build(self):
        """
        Builds ``UBuilder`` into ``U``.

        Returns:
            ``U`` for ``UBuilder``.
        """

        number = self.number
        if isinstance(self.number, types.Integer):
            number = self.number
        elif isinstance(self.number, int):
            number = types.Integer(self.number)
        elif isinstance(self.number, str):
            number = types.Integer.from_mcnp(self.number)

        return U(
            number=number,
        )

    @staticmethod
    def unbuild(ast: U):
        """
        Unbuilds ``U`` into ``UBuilder``

        Returns:
            ``UBuilder`` for ``U``.
        """

        return UBuilder(
            number=copy.deepcopy(ast.number),
        )
