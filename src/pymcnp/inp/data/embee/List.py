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
        'reactions': types.Real,
    }

    _REGEX = re.compile(r'list( \S+)')

    def __init__(self, reactions: types.Real):
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

        self.reactions: typing.Final[types.Real] = reactions
