import re
import typing
import dataclasses


from ._option import SsrOption
from ....utils import types
from ....utils import errors


class Ext(SsrOption, keyword='ext'):
    """
    Represents INP ext elements.

    Attributes:
        number: Distribution number for baising sampling.
    """

    _ATTRS = {
        'number': types.DistributionNumber,
    }

    _REGEX = re.compile(rf'\Aext( {types.DistributionNumber._REGEX.pattern})\Z')

    def __init__(self, number: types.DistributionNumber):
        """
        Initializes ``Ext``.

        Parameters:
            number: Distribution number for baising sampling.

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

        self.number: typing.Final[types.DistributionNumber] = number


@dataclasses.dataclass
class ExtBuilder:
    """
    Builds ``Ext``.

    Attributes:
        number: Distribution number for baising sampling.
    """

    number: str | types.DistributionNumber

    def build(self):
        """
        Builds ``ExtBuilder`` into ``Ext``.

        Returns:
            ``Ext`` for ``ExtBuilder``.
        """

        if isinstance(self.number, types.DistributionNumber):
            number = self.number
        elif isinstance(self.number, str):
            number = types.DistributionNumber.from_mcnp(self.number)

        return Ext(
            number=number,
        )
