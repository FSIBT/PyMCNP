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
        'stride': types.Integer,
    }

    _REGEX = re.compile(r'stride( \S+)')

    def __init__(self, stride: types.Integer):
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

        self.stride: typing.Final[types.Integer] = stride
