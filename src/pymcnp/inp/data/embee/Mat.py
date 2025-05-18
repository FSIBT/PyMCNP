import re
import typing
import dataclasses


from ._option import EmbeeOption
from ....utils import types
from ....utils import errors


class Mat(EmbeeOption):
    """
    Represents INP mat elements.

    Attributes:
        number: Material number.
    """

    _ATTRS = {
        'number': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Amat( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, number: types.IntegerOrJump):
        """
        Initializes ``Mat``.

        Parameters:
            number: Material number.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if number is None or not (0 <= number <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, number)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                number,
            ]
        )

        self.number: typing.Final[types.IntegerOrJump] = number


@dataclasses.dataclass
class MatBuilder:
    """
    Builds ``Mat``.

    Attributes:
        number: Material number.
    """

    number: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``MatBuilder`` into ``Mat``.

        Returns:
            ``Mat`` for ``MatBuilder``.
        """

        number = self.number
        if isinstance(self.number, types.Integer):
            number = self.number
        elif isinstance(self.number, int):
            number = types.IntegerOrJump(self.number)
        elif isinstance(self.number, str):
            number = types.IntegerOrJump.from_mcnp(self.number)

        return Mat(
            number=number,
        )
