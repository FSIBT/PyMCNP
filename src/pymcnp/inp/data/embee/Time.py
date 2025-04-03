import re
import typing


from .option_ import EmbeeOption_
from ....utils import types
from ....utils import errors


class Time(EmbeeOption_, keyword='time'):
    """
    Represents INP time elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'factor': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Atime( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, factor: types.RealOrJump):
        """
        Initializes ``Time``.

        Parameters:
            factor: Multiplicative conversion factor for time-related output.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if factor is None or not (factor > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, factor)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                factor,
            ]
        )

        self.factor: typing.Final[types.RealOrJump] = factor
