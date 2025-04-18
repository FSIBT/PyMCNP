import re
import typing


from .option_ import EmbedOption_
from ....utils import types
from ....utils import errors


class Length(EmbedOption_, keyword='length'):
    """
    Represents INP length elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'factor': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Alength( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, factor: types.RealOrJump):
        """
        Initializes ``Length``.

        Parameters:
            factor: Conversion factor to centimeters for all mesh dimentions.

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
