import re
import typing
import dataclasses


from ._option import SdefOption
from ....utils import types
from ....utils import errors


class Tr_0(SdefOption):
    """
    Represents INP tr variation #0 elements.

    Attributes:
        number: Particle weight.
    """

    _ATTRS = {
        'number': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Atr( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, number: types.IntegerOrJump):
        """
        Initializes ``Tr_0``.

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
class TrBuilder_0:
    """
    Builds ``Tr_0``.

    Attributes:
        number: Particle weight.
    """

    number: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``TrBuilder_0`` into ``Tr_0``.

        Returns:
            ``Tr_0`` for ``TrBuilder_0``.
        """

        number = self.number
        if isinstance(self.number, types.Integer):
            number = self.number
        elif isinstance(self.number, int):
            number = types.IntegerOrJump(self.number)
        elif isinstance(self.number, str):
            number = types.IntegerOrJump.from_mcnp(self.number)

        return Tr_0(
            number=number,
        )
