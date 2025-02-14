import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class PtracOption_Tally(_option.PtracOption_, keyword='tally'):
    """
    Represents INP data card data option tally options.

    Attributes:
        numbers: List of tally numbers for filtering.
    """

    _REGEX = re.compile(r'\Atally(( \S+)+)\Z')

    def __init__(self, numbers: tuple[types.Integer]):
        """
        Initializes ``PtracOption_Tally``.

        Parameters:
            numbers: List of tally numbers for filtering.

        Returns:
            ``PtracOption_Tally``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if numbers is None or not (filter(lambda entry: not (entry != 0), numbers)):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, numbers)

        self.value: typing.Final[tuple[any]] = types._Tuple([numbers])
        self.numbers: typing.Final[tuple[types.Integer]] = numbers

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``PtracOption_Tally`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``PtracOption_Tally``.

        Raises:
            McnpError: SYNTAX_PTRAC_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = PtracOption_Tally._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_PTRAC_OPTION, source)

        numbers = types._Tuple(
            [types.Integer.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[1])]
        )

        return PtracOption_Tally(numbers)
