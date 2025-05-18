import re
import typing
import dataclasses


from ._option import SdefOption
from ....utils import types
from ....utils import errors


class Sur(SdefOption):
    """
    Represents INP sur elements.

    Attributes:
        number: Surface number.
    """

    _ATTRS = {
        'number': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Asur( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, number: types.IntegerOrJump):
        """
        Initializes ``Sur``.

        Parameters:
            number: Surface number.

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
class SurBuilder:
    """
    Builds ``Sur``.

    Attributes:
        number: Surface number.
    """

    number: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``SurBuilder`` into ``Sur``.

        Returns:
            ``Sur`` for ``SurBuilder``.
        """

        number = self.number
        if isinstance(self.number, types.Integer):
            number = self.number
        elif isinstance(self.number, int):
            number = types.IntegerOrJump(self.number)
        elif isinstance(self.number, str):
            number = types.IntegerOrJump.from_mcnp(self.number)

        return Sur(
            number=number,
        )
