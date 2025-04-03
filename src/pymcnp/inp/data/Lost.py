import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Lost(DataOption_, keyword='lost'):
    """
    Represents INP lost elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'lost1': types.IntegerOrJump,
        'lost2': types.IntegerOrJump,
    }

    _REGEX = re.compile(
        rf'\Alost( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})\Z'
    )

    def __init__(self, lost1: types.IntegerOrJump, lost2: types.IntegerOrJump):
        """
        Initializes ``Lost``.

        Parameters:
            lost1: Number of particles which can be lost before job termination.
            lost2: Maximum number of debug prints for lost particles..

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if lost1 is None or not (lost1 >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, lost1)
        if lost2 is None or not (lost2 >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, lost2)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                lost1,
                lost2,
            ]
        )

        self.lost1: typing.Final[types.IntegerOrJump] = lost1
        self.lost2: typing.Final[types.IntegerOrJump] = lost2
