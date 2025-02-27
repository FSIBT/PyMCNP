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
        'cutoff': types.Real,
    }

    _REGEX = re.compile(r'pecut( \S+)')

    def __init__(self, cutoff: types.Real):
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

        self.cutoff: typing.Final[types.Real] = cutoff
