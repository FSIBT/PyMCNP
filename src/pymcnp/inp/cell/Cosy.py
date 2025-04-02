import re
import typing


from .option_ import CellOption_
from ...utils import types
from ...utils import errors


class Cosy(CellOption_, keyword='cosy'):
    """
    Represents INP cosy elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'number': types.Integer,
    }

    _REGEX = re.compile(rf'\Acosy( {types.Integer._REGEX.pattern})\Z')

    def __init__(self, number: types.Integer):
        """
        Initializes ``Cosy``.

        Parameters:
            number: Cell cosy map number.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if number is None or number.value not in {1, 2, 3, 4, 5, 6}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, number)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                number,
            ]
        )

        self.number: typing.Final[types.Integer] = number
