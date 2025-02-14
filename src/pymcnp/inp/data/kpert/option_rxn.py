import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class KpertOption_Rxn(_option.KpertOption_, keyword='rxn'):
    """
    Represents INP data card data option rxn options.

    Attributes:
        numbers: List of reaction numbers for pertubation.
    """

    _REGEX = re.compile(r'\Arxn(( \S+)+)\Z')

    def __init__(self, numbers: tuple[types.Integer]):
        """
        Initializes ``KpertOption_Rxn``.

        Parameters:
            numbers: List of reaction numbers for pertubation.

        Returns:
            ``KpertOption_Rxn``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if numbers is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, numbers)

        self.value: typing.Final[tuple[any]] = types._Tuple([numbers])
        self.numbers: typing.Final[tuple[types.Integer]] = numbers

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``KpertOption_Rxn`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``KpertOption_Rxn``.

        Raises:
            McnpError: SYNTAX_KPERT_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = KpertOption_Rxn._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_KPERT_OPTION, source)

        numbers = types._Tuple(
            [types.Integer.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[1])]
        )

        return KpertOption_Rxn(numbers)
