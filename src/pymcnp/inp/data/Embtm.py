import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Embtm(DataOption_, keyword='embtm'):
    """
    Represents INP embtm elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'multipliers': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(rf'\Aembtm(\d+)((?: {types.RealOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, suffix: types.Integer, multipliers: types.Tuple[types.RealOrJump]):
        """
        Initializes ``Embtm``.

        Parameters:
            suffix: Data card option suffix.
            multipliers: Tuple of time multipliers.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if multipliers is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, multipliers)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                multipliers,
            ]
        )

        self.suffix: typing.Final[types.IntegerOrJump] = suffix
        self.multipliers: typing.Final[types.Tuple[types.RealOrJump]] = multipliers
