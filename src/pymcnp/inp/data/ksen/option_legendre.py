import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class KsenOption_Legendre(_option.KsenOption_, keyword='legendre'):
    """
    Represents INP data card data option legendre options.

    Attributes:
        number: Order of Legendre moments to calculate sensitivities.
    """

    _REGEX = re.compile(r'\Alegendre( \S+)\Z')

    def __init__(self, number: types.Integer):
        """
        Initializes ``KsenOption_Legendre``.

        Parameters:
            number: Order of Legendre moments to calculate sensitivities.

        Returns:
            ``KsenOption_Legendre``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if number is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, number)

        self.value: typing.Final[tuple[any]] = types._Tuple([number])
        self.number: typing.Final[types.Integer] = number

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``KsenOption_Legendre`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``KsenOption_Legendre``.

        Raises:
            InpError: SYNTAX_KSEN_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = KsenOption_Legendre._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        number = types.Integer.from_mcnp(tokens[1])

        return KsenOption_Legendre(number)
