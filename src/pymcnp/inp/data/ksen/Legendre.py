import re
import typing
import dataclasses


from .option_ import KsenOption_
from ....utils import types
from ....utils import errors


class Legendre(KsenOption_, keyword='legendre'):
    """
    Represents INP legendre elements.

    Attributes:
        number: Order of Legendre moments to calculate sensitivities.
    """

    _ATTRS = {
        'number': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Alegendre( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, number: types.IntegerOrJump):
        """
        Initializes ``Legendre``.

        Parameters:
            number: Order of Legendre moments to calculate sensitivities.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if number is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, number)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                number,
            ]
        )

        self.number: typing.Final[types.IntegerOrJump] = number


@dataclasses.dataclass
class LegendreBuilder:
    """
    Builds ``Legendre``.

    Attributes:
        number: Order of Legendre moments to calculate sensitivities.
    """

    number: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``LegendreBuilder`` into ``Legendre``.

        Returns:
            ``Legendre`` for ``LegendreBuilder``.
        """

        if isinstance(self.number, types.Integer):
            number = self.number
        elif isinstance(self.number, int):
            number = types.IntegerOrJump(self.number)
        elif isinstance(self.number, str):
            number = types.IntegerOrJump.from_mcnp(self.number)

        return Legendre(
            number=number,
        )
