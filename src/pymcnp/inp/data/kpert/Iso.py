import re
import typing


from .option_ import KpertOption_
from ....utils import types
from ....utils import errors


class Iso(KpertOption_, keyword='iso'):
    """
    Represents INP iso elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'zaids': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Aiso((?: {types.Real._REGEX.pattern})+?)\Z')

    def __init__(self, zaids: types.Tuple[types.Real]):
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

        self.zaids: typing.Final[types.Tuple[types.Real]] = zaids
