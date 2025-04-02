import re
import typing


from .option_ import SsrOption_
from ....utils import types
from ....utils import errors


class Ext(SsrOption_, keyword='ext'):
    """
    Represents INP ext elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
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
