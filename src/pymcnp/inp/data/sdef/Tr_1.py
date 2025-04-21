import re
import typing
import dataclasses


from ._option import SdefOption
from ....utils import types
from ....utils import errors


class Tr_1(SdefOption, keyword='tr'):
    """
    Represents INP tr variation #1 elements.

    Attributes:
        number: Particle weight.
    """

    _ATTRS = {
        'number': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Atr( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, number: types.IntegerOrJump):
        """
        Initializes ``Tr_1``.

        Parameters:
            number: Particle weight.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if number is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, number)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                number,
            ]
        )

        self.number: typing.Final[types.IntegerOrJump] = number


@dataclasses.dataclass
class TrBuilder_1:
    """
    Builds ``Tr_1``.

    Attributes:
        number: Particle weight.
    """

    number: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``TrBuilder_1`` into ``Tr_1``.

        Returns:
            ``Tr_1`` for ``TrBuilder_1``.
        """

        if isinstance(self.number, types.Integer):
            number = self.number
        elif isinstance(self.number, int):
            number = types.IntegerOrJump(self.number)
        elif isinstance(self.number, str):
            number = types.IntegerOrJump.from_mcnp(self.number)

        return Tr_1(
            number=number,
        )
