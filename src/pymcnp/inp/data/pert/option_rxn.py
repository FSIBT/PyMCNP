import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class PertOption_Rxn(_option.PertOption_, keyword='rxn'):
    """
    Represents INP data card data option rxn options.

    Attributes:
        numbers: ENDF/B reaction number.
    """

    _REGEX = re.compile(r'\Arxn(( \S+)+)\Z')

    def __init__(self, numbers: tuple[types.Integer]):
        """
        Initializes ``PertOption_Rxn``.

        Parameters:
            numbers: ENDF/B reaction number.

        Returns:
            ``PertOption_Rxn``.

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
        Generates ``PertOption_Rxn`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``PertOption_Rxn``.

        Raises:
            InpError: SYNTAX_PERT_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = PertOption_Rxn._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        numbers = types._Tuple(
            [types.Integer.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[1])]
        )

        return PertOption_Rxn(numbers)
