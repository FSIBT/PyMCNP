import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class RandOption_Stride(_option.RandOption_, keyword='stride'):
    """
    Represents INP data card data option stride options.

    Attributes:
        stride: Number of random numbers between source particle.
    """

    _REGEX = re.compile(r'\Astride( \S+)\Z')

    def __init__(self, stride: types.Integer):
        """
        Initializes ``RandOption_Stride``.

        Parameters:
            stride: Number of random numbers between source particle.

        Returns:
            ``RandOption_Stride``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if stride is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, stride)

        self.value: typing.Final[tuple[any]] = types._Tuple([stride])
        self.stride: typing.Final[types.Integer] = stride

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``RandOption_Stride`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``RandOption_Stride``.

        Raises:
            McnpError: SYNTAX_RAND_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = RandOption_Stride._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_RAND_OPTION, source)

        stride = types.Integer.from_mcnp(tokens[1])

        return RandOption_Stride(stride)
