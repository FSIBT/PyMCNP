import re
import typing


from .option_ import RandOption_
from ....utils import types
from ....utils import errors


class Stride(RandOption_, keyword='stride'):
    """
    Represents INP stride elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'stride': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Astride( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, stride: types.IntegerOrJump):
        """
        Initializes ``Stride``.

        Parameters:
            stride: Number of random numbers between source particle.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if stride is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, stride)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                stride,
            ]
        )

        self.stride: typing.Final[types.IntegerOrJump] = stride
