import re
import typing
import dataclasses


from ._option import CellOption
from ...utils import types
from ...utils import errors


class Bflcl(CellOption, keyword='bflcl'):
    """
    Represents INP bflcl elements.

    Attributes:
        number: Cell magnetic field number.
    """

    _ATTRS = {
        'number': types.Integer,
    }

    _REGEX = re.compile(rf'\Abflcl( {types.Integer._REGEX.pattern})\Z')

    def __init__(self, number: types.Integer):
        """
        Initializes ``Bflcl``.

        Parameters:
            number: Cell magnetic field number.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if number is None or not (number >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, number)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                number,
            ]
        )

        self.number: typing.Final[types.Integer] = number


@dataclasses.dataclass
class BflclBuilder:
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

        if isinstance(self.number, types.Integer):
            number = self.number
        elif isinstance(self.number, int):
            number = types.Integer(self.number)
        elif isinstance(self.number, str):
            number = types.Integer.from_mcnp(self.number)

        return Bflcl(
            number=number,
        )
