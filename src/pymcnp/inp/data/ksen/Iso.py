import re
import typing


from .option_ import KsenOption_
from ....utils import types
from ....utils import errors


class Iso(KsenOption_, keyword='iso'):
    """
    Represents INP iso elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'zaids': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(rf'\Aiso((?: {types.RealOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, zaids: types.Tuple[types.RealOrJump]):
        """
        Initializes ``Iso``.

        Parameters:
            zaids: List of ZAIDs for pertubation.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if zaids is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, zaids)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                zaids,
            ]
        )

        self.zaids: typing.Final[types.Tuple[types.RealOrJump]] = zaids
