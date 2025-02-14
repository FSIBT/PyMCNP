import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class RandOption_Seed(_option.RandOption_, keyword='seed'):
    """
    Represents INP data card data option seed options.

    Attributes:
        seed: Random number generator seed.
    """

    _REGEX = re.compile(r'\Aseed( \S+)\Z')

    def __init__(self, seed: types.Integer):
        """
        Initializes ``RandOption_Seed``.

        Parameters:
            seed: Random number generator seed.

        Returns:
            ``RandOption_Seed``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if seed is None or not (seed.value % 2 == 1):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, seed)

        self.value: typing.Final[tuple[any]] = types._Tuple([seed])
        self.seed: typing.Final[types.Integer] = seed

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``RandOption_Seed`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``RandOption_Seed``.

        Raises:
            McnpError: SYNTAX_RAND_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = RandOption_Seed._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_RAND_OPTION, source)

        seed = types.Integer.from_mcnp(tokens[1])

        return RandOption_Seed(seed)
