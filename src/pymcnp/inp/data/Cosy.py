import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Cosy(DataOption_, keyword='cosy'):
    """
    Represents INP cosy elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'numbers': types.Tuple[types.IntegerOrJump],
    }

    _REGEX = re.compile(rf'\Acosy((?: {types.IntegerOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, numbers: types.Tuple[types.IntegerOrJump]):
        """
        Initializes ``Cosy``.

        Parameters:
            numbers: Tuple of COSY map numbers.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if numbers is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, numbers)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                numbers,
            ]
        )

        self.numbers: typing.Final[types.Tuple[types.IntegerOrJump]] = numbers
