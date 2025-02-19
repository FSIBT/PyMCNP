import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class KsenOption_Rxn(_option.KsenOption_, keyword='rxn'):
    """
    Represents INP data card data option rxn options.

    Attributes:
        numbers: List of reaction numbers for pertubation.
    """

    _REGEX = re.compile(r'\Arxn(( \S+)+)\Z')

    def __init__(self, numbers: tuple[types.Integer]):
        """
        Initializes ``KsenOption_Rxn``.

        Parameters:
            numbers: List of reaction numbers for pertubation.

        Returns:
            ``KsenOption_Rxn``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if numbers is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, numbers)

        self.value: typing.Final[tuple[any]] = types._Tuple([numbers])
        self.numbers: typing.Final[tuple[types.Integer]] = numbers

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``KsenOption_Rxn`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``KsenOption_Rxn``.

        Raises:
            InpError: SYNTAX_KSEN_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = KsenOption_Rxn._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        numbers = types._Tuple(
            [types.Integer.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[1])]
        )

        return KsenOption_Rxn(numbers)
