import re
import typing


from .option_ import SsrOption_
from ....utils import types
from ....utils import errors


class Tr_1(SsrOption_, keyword='tr'):
    """
    Represents INP tr_1 elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'number': types.Integer,
    }

    _REGEX = re.compile(rf'tr( {types.Integer._REGEX.pattern})')

    def __init__(self, number: types.Integer):
        """
        Initializes ``Tr_1``.

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

        self.number: typing.Final[types.Integer] = number
