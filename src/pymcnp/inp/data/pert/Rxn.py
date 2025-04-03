import re
import typing


from .option_ import PertOption_
from ....utils import types
from ....utils import errors


class Rxn(PertOption_, keyword='rxn'):
    """
    Represents INP rxn elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'numbers': types.Tuple[types.IntegerOrJump],
    }

    _REGEX = re.compile(rf'\Arxn((?: {types.IntegerOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, numbers: types.Tuple[types.IntegerOrJump]):
        """
        Initializes ``Rxn``.

        Parameters:
            numbers: ENDF/B reaction number.

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
