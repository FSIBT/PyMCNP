import re
import typing
import dataclasses


from ._option import EmbeeOption
from ....utils import types
from ....utils import errors


class Embed(EmbeeOption):
    """
    Represents INP embed elements.

    Attributes:
        number: Embedded mesh universe number.
    """

    _ATTRS = {
        'number': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Aembed( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, number: types.IntegerOrJump):
        """
        Initializes ``Embed``.

        Parameters:
            number: Embedded mesh universe number.

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
class EmbedBuilder:
    """
    Builds ``Embed``.

    Attributes:
        number: Embedded mesh universe number.
    """

    number: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``EmbedBuilder`` into ``Embed``.

        Returns:
            ``Embed`` for ``EmbedBuilder``.
        """

        if isinstance(self.number, types.Integer):
            number = self.number
        elif isinstance(self.number, int):
            number = types.IntegerOrJump(self.number)
        elif isinstance(self.number, str):
            number = types.IntegerOrJump.from_mcnp(self.number)

        return Embed(
            number=number,
        )
