import re
import typing


from .option_ import ActOption_
from ....utils import types
from ....utils import errors


class Pecut(ActOption_, keyword='pecut'):
    """
    Represents INP pecut elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'cutoff': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Apecut( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, cutoff: types.RealOrJump):
        """
        Initializes ``Pecut``.

        Parameters:
            cutoff: Delayed-gamma energy cutoff.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if cutoff is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, cutoff)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                cutoff,
            ]
        )

        self.cutoff: typing.Final[types.RealOrJump] = cutoff
