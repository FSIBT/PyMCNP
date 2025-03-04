import re
import typing


from .option_ import SsrOption_
from ....utils import types
from ....utils import errors


class Tr_0(SsrOption_, keyword='tr'):
    """
    Represents INP tr_0 elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'number': types.DistributionNumber,
    }

    _REGEX = re.compile(r'tr( \S+)')

    def __init__(self, number: types.DistributionNumber):
        """
        Initializes ``Tr_0``.

        Parameters:
            number: Particle weight.

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
