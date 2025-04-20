import re
import typing
import dataclasses


from .option_ import FmeshOption_
from ....utils import types
from ....utils import errors


class Tr(FmeshOption_, keyword='tr'):
    """
    Represents INP tr elements.

    Attributes:
        number: Transformation applied to the mesh.
    """

    _ATTRS = {
        'number': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Atr( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, number: types.IntegerOrJump):
        """
        Initializes ``Tr``.

        Parameters:
            number: Transformation applied to the mesh.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if number is None or not (1 <= number <= 999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, number)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                number,
            ]
        )

        self.number: typing.Final[types.IntegerOrJump] = number


@dataclasses.dataclass
class TrBuilder:
    """
    Builds ``Tr``.

    Attributes:
        number: Transformation applied to the mesh.
    """

    number: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``TrBuilder`` into ``Tr``.

        Returns:
            ``Tr`` for ``TrBuilder``.
        """

        if isinstance(self.number, types.Integer):
            number = self.number
        elif isinstance(self.number, int):
            number = types.IntegerOrJump(self.number)
        elif isinstance(self.number, str):
            number = types.IntegerOrJump.from_mcnp(self.number)

        return Tr(
            number=number,
        )
