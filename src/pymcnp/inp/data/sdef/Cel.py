import re
import typing


from .option_ import SdefOption_
from ....utils import types
from ....utils import errors


class Cel(SdefOption_, keyword='cel'):
    """
    Represents INP cel elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'number': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Acel( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, number: types.IntegerOrJump):
        """
        Initializes ``Cel``.

        Parameters:
            number: Cell number.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if number is None or not (isinstance(number.value, types.Jump) or 0 <= number.value <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, number)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                number,
            ]
        )

        self.number: typing.Final[types.IntegerOrJump] = number
