import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class PtracOption_Surface(_option.PtracOption_, keyword='surface'):
    """
    Represents INP data card data option surface options.

    Attributes:
        numbers: List of surface numbers for filtering.
    """

    _REGEX = re.compile(r'\Asurface(( \S+)+)\Z')

    def __init__(self, numbers: tuple[types.Integer]):
        """
        Initializes ``PtracOption_Surface``.

        Parameters:
            numbers: List of surface numbers for filtering.

        Returns:
            ``PtracOption_Surface``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if numbers is None or not (filter(lambda entry: not (1 <= entry <= 99_999_999), numbers)):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, numbers)

        self.value: typing.Final[tuple[any]] = types._Tuple([numbers])
        self.numbers: typing.Final[tuple[types.Integer]] = numbers

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``PtracOption_Surface`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``PtracOption_Surface``.

        Raises:
            InpError: SYNTAX_PTRAC_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = PtracOption_Surface._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        numbers = types._Tuple(
            [types.Integer.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[1])]
        )

        return PtracOption_Surface(numbers)
