import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class RandOption_Hist(_option.RandOption_, keyword='hist'):
    """
    Represents INP data card data option hist options.

    Attributes:
        hist: Starting pseudorandom number.
    """

    _REGEX = re.compile(r'\Ahist( \S+)\Z')

    def __init__(self, hist: types.Integer):
        """
        Initializes ``RandOption_Hist``.

        Parameters:
            hist: Starting pseudorandom number.

        Returns:
            ``RandOption_Hist``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if hist is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, hist)

        self.value: typing.Final[tuple[any]] = types._Tuple([hist])
        self.hist: typing.Final[types.Integer] = hist

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``RandOption_Hist`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``RandOption_Hist``.

        Raises:
            McnpError: SYNTAX_RAND_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = RandOption_Hist._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_RAND_OPTION, source)

        hist = types.Integer.from_mcnp(tokens[1])

        return RandOption_Hist(hist)
