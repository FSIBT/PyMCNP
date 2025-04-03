import re
import typing


from .option_ import EmbeeOption_
from ....utils import types
from ....utils import errors


class Factor(EmbeeOption_, keyword='factor'):
    """
    Represents INP factor elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'constant': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Afactor( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, constant: types.RealOrJump):
        """
        Initializes ``Factor``.

        Parameters:
            constant: Multiplicative constant.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if constant is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, constant)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                constant,
            ]
        )

        self.constant: typing.Final[types.RealOrJump] = constant
