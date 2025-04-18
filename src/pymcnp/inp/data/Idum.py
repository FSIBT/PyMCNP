import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Idum(DataOption_, keyword='idum'):
    """
    Represents INP idum elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'intergers': types.Tuple[types.IntegerOrJump],
    }

    _REGEX = re.compile(rf'\Aidum((?: {types.IntegerOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, intergers: types.Tuple[types.IntegerOrJump]):
        """
        Initializes ``Idum``.

        Parameters:
            intergers: Integer array.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if intergers is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, intergers)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                intergers,
            ]
        )

        self.intergers: typing.Final[types.Tuple[types.IntegerOrJump]] = intergers
