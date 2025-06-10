import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Ccc(_option.SdefOption):
    """
    Represents INP ccc elements.

    Attributes:
        number: Cookie-cutter cell number.
    """

    _KEYWORD = 'ccc'

    _ATTRS = {
        'number': types.Integer,
    }

    _REGEX = re.compile(rf'\Accc( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, number: types.Integer):
        """
        Initializes ``Ccc``.

        Parameters:
            number: Cookie-cutter cell number.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if number is None or not (0 <= number.value <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, number)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                number,
            ]
        )

        self.number: typing.Final[types.Integer] = number


@dataclasses.dataclass
class CccBuilder(_option.SdefOptionBuilder):
    """
    Builds ``Ccc``.

    Attributes:
        number: Cookie-cutter cell number.
    """

    number: str | int | types.Integer

    def build(self):
        """
        Builds ``CccBuilder`` into ``Ccc``.

        Returns:
            ``Ccc`` for ``CccBuilder``.
        """

        number = self.number
        if isinstance(self.number, types.Integer):
            number = self.number
        elif isinstance(self.number, int):
            number = types.Integer(self.number)
        elif isinstance(self.number, str):
            number = types.Integer.from_mcnp(self.number)

        return Ccc(
            number=number,
        )

    @staticmethod
    def unbuild(ast: Ccc):
        """
        Unbuilds ``Ccc`` into ``CccBuilder``

        Returns:
            ``CccBuilder`` for ``Ccc``.
        """

        return CccBuilder(
            number=copy.deepcopy(ast.number),
        )
