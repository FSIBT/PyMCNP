import re
import typing


from .option_ import ActOption_
from ....utils import types
from ....utils import errors


class Hlcut(ActOption_, keyword='hlcut'):
    """
    Represents INP hlcut elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'cutoff': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Ahlcut( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, cutoff: types.RealOrJump):
        """
        Initializes ``Hlcut``.

        Parameters:
            cutoff: Spontaneous-decay half-life threshold.

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
