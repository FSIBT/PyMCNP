import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Cel(_option.SdefOption):
    """
    Represents INP cel elements.

    Attributes:
        number: Cell number.
    """

    _KEYWORD = 'cel'

    _ATTRS = {
        'number': types.Integer,
    }

    _REGEX = re.compile(rf'\Acel( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, number: types.Integer):
        """
        Initializes ``Cel``.

        Parameters:
            number: Cell number.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if number is None or not (isinstance(number.value, types.Jump) or (number >= 0 and number <= 99_999_999)):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, number)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                number,
            ]
        )

        self.number: typing.Final[types.Integer] = number


@dataclasses.dataclass
class CelBuilder(_option.SdefOptionBuilder):
    """
    Builds ``Cel``.

    Attributes:
        number: Cell number.
    """

    number: str | int | types.Integer

    def build(self):
        """
        Builds ``CelBuilder`` into ``Cel``.

        Returns:
            ``Cel`` for ``CelBuilder``.
        """

        number = self.number
        if isinstance(self.number, types.Integer):
            number = self.number
        elif isinstance(self.number, int):
            number = types.Integer(self.number)
        elif isinstance(self.number, str):
            number = types.Integer.from_mcnp(self.number)

        return Cel(
            number=number,
        )

    @staticmethod
    def unbuild(ast: Cel):
        """
        Unbuilds ``Cel`` into ``CelBuilder``

        Returns:
            ``CelBuilder`` for ``Cel``.
        """

        return CelBuilder(
            number=copy.deepcopy(ast.number),
        )
