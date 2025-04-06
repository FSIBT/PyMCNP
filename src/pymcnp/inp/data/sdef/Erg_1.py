import re
import typing


from .option_ import SdefOption_
from ....utils import types
from ....utils import errors


class Erg_1(SdefOption_, keyword='erg'):
    """
    Represents INP erg elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'energy': types.DistributionNumber,
    }

    _REGEX = re.compile(rf'\Aerg( {types.DistributionNumber._REGEX.pattern})\Z')

    def __init__(self, energy: types.DistributionNumber):
        """
        Initializes ``Erg_1``.

        Parameters:
            energy: Kinetic energy.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if energy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, energy)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                energy,
            ]
        )

        self.energy: typing.Final[types.DistributionNumber] = energy
