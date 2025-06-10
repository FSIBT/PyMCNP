import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Bflcl(_option.CellOption):
    """
    Represents INP bflcl elements.

    Attributes:
        number: Cell magnetic field number.
    """

    _KEYWORD = 'bflcl'

    _ATTRS = {
        'number': types.Integer,
    }

    _REGEX = re.compile(rf'\Abflcl( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, number: types.Integer):
        """
        Initializes ``Bflcl``.

        Parameters:
            number: Cell magnetic field number.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if number is None or not (number.value >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, number)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                number,
            ]
        )

        self.number: typing.Final[types.Integer] = number


@dataclasses.dataclass
class BflclBuilder(_option.CellOptionBuilder):
    """
    Builds ``Bflcl``.

    Attributes:
        number: Cell magnetic field number.
    """

    number: str | int | types.Integer

    def build(self):
        """
        Builds ``BflclBuilder`` into ``Bflcl``.

        Returns:
            ``Bflcl`` for ``BflclBuilder``.
        """

        number = self.number
        if isinstance(self.number, types.Integer):
            number = self.number
        elif isinstance(self.number, int):
            number = types.Integer(self.number)
        elif isinstance(self.number, str):
            number = types.Integer.from_mcnp(self.number)

        return Bflcl(
            number=number,
        )

    @staticmethod
    def unbuild(ast: Bflcl):
        """
        Unbuilds ``Bflcl`` into ``BflclBuilder``

        Returns:
            ``BflclBuilder`` for ``Bflcl``.
        """

        return BflclBuilder(
            number=copy.deepcopy(ast.number),
        )
