import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class SsrOption_Ext(_option.SsrOption_, keyword='ext'):
    """
    Represents INP data card data option ext options.

    Attributes:
        number: Distribution number for baising sampling.
    """

    _REGEX = re.compile(r'\Aext( \S+)\Z')

    def __init__(self, number: types.DistributionNumber):
        """
        Initializes ``SsrOption_Ext``.

        Parameters:
            number: Distribution number for baising sampling.

        Returns:
            ``SsrOption_Ext``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if number is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, number)

        self.value: typing.Final[tuple[any]] = types._Tuple([number])
        self.number: typing.Final[types.DistributionNumber] = number

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SsrOption_Ext`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``SsrOption_Ext``.

        Raises:
            InpError: SYNTAX_SSR_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SsrOption_Ext._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        number = types.DistributionNumber.from_mcnp(tokens[1])

        return SsrOption_Ext(number)
