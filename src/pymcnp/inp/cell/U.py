import re
import typing


from .option_ import CellOption_
from ...utils import types
from ...utils import errors


class U(CellOption_, keyword='u'):
    """
    Represents INP u elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'number': types.Integer,
    }

    _REGEX = re.compile(rf'u( {types.Integer._REGEX.pattern})')

    def __init__(self, number: types.Integer):
        """
        Initializes ``U``.

        Parameters:
            number: Cell universe number.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if number is None or not (-99_999_999 <= number <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, number)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                number,
            ]
        )

        self.number: typing.Final[types.Integer] = number
