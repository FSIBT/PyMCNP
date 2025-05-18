import re
import typing
import dataclasses


from ._option import SdefOption
from ....utils import types
from ....utils import errors


class Cel(SdefOption):
    """
    Represents INP cel elements.

    Attributes:
        number: Cell number.
    """

    _ATTRS = {
        'number': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Acel( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, number: types.IntegerOrJump):
        """
        Initializes ``Cel``.

        Parameters:
            number: Cell number.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if number is None or not (
            isinstance(number.value, types.Jump) or 0 <= number.value <= 99_999_999
        ):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, number)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                number,
            ]
        )

        self.number: typing.Final[types.IntegerOrJump] = number


@dataclasses.dataclass
class CelBuilder:
    """
    Builds ``Cel``.

    Attributes:
        number: Cell number.
    """

    number: str | int | types.IntegerOrJump

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
            number = types.IntegerOrJump(self.number)
        elif isinstance(self.number, str):
            number = types.IntegerOrJump.from_mcnp(self.number)

        return Cel(
            number=number,
        )
