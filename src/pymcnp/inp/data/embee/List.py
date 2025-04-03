import re
import typing


from .option_ import EmbeeOption_
from ....utils import types
from ....utils import errors


class List(EmbeeOption_, keyword='list'):
    """
    Represents INP list elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'reactions': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Alist( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, reactions: types.RealOrJump):
        """
        Initializes ``List``.

        Parameters:
            reactions: List of reactions.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if reactions is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, reactions)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                reactions,
            ]
        )

        self.reactions: typing.Final[types.RealOrJump] = reactions
