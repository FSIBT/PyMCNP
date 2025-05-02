import re
import typing
import dataclasses


from ._option import SsrOption
from ....utils import types
from ....utils import errors


class Tr_0(SsrOption):
    """
    Represents INP tr variation #0 elements.

    Attributes:
        number: Particle weight.
    """

    _ATTRS = {
        'number': types.DistributionNumber,
    }

    _REGEX = re.compile(rf'\Atr( {types.DistributionNumber._REGEX.pattern})\Z')

    def __init__(self, number: types.DistributionNumber):
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

        self.number: typing.Final[types.DistributionNumber] = number


@dataclasses.dataclass
class TrBuilder_0:
    """
    Builds ``Tr_0``.

    Attributes:
        number: Particle weight.
    """

    number: str | types.DistributionNumber

    def build(self):
        """
        Builds ``TrBuilder_0`` into ``Tr_0``.

        Returns:
            ``Tr_0`` for ``TrBuilder_0``.
        """

        if isinstance(self.number, types.DistributionNumber):
            number = self.number
        elif isinstance(self.number, str):
            number = types.DistributionNumber.from_mcnp(self.number)

        return Tr_0(
            number=number,
        )
