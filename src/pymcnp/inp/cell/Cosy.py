import re
import typing
import dataclasses


from .option_ import CellOption_
from ...utils import types
from ...utils import errors


class Cosy(CellOption_, keyword='cosy'):
    """
    Represents INP cosy elements.

    Attributes:
        number: Cell cosy map number.
    """

    _ATTRS = {
        'number': types.Integer,
    }

    _REGEX = re.compile(rf'\Acosy( {types.Integer._REGEX.pattern})\Z')

    def __init__(self, number: types.Integer):
        """
        Initializes ``Cosy``.

        Parameters:
            number: Cell cosy map number.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if number is None or number.value not in {1, 2, 3, 4, 5, 6}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, number)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                number,
            ]
        )

        self.number: typing.Final[types.Integer] = number


@dataclasses.dataclass
class CosyBuilder:
    """
    Builds ``Cosy``.

    Attributes:
        number: Cell cosy map number.
    """

    number: str | int | types.Integer

    def build(self):
        """
        Builds ``CosyBuilder`` into ``Cosy``.

        Returns:
            ``Cosy`` for ``CosyBuilder``.
        """

        if isinstance(self.number, types.Integer):
            number = self.number
        elif isinstance(self.number, int):
            number = types.Integer(self.number)
        elif isinstance(self.number, str):
            number = types.Integer.from_mcnp(self.number)

        return Cosy(
            number=number,
        )
