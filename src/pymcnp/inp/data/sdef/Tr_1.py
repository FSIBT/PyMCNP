import re
import typing


from .option_ import SdefOption_
from ....utils import types
from ....utils import errors


class Tr_1(SdefOption_, keyword='tr'):
    """
    Represents INP tr_1 elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
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
