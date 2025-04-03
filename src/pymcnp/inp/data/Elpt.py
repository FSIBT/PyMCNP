import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Elpt(DataOption_, keyword='elpt'):
    """
    Represents INP elpt elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'cutoffs': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(rf'\Aelpt((?: {types.RealOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, cutoffs: types.Tuple[types.RealOrJump]):
        """
        Initializes ``Elpt``.

        Parameters:
            cutoffs: Tuple of cell lower energy cutoffs.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if cutoffs is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, cutoffs)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                cutoffs,
            ]
        )

        self.cutoffs: typing.Final[types.Tuple[types.RealOrJump]] = cutoffs
