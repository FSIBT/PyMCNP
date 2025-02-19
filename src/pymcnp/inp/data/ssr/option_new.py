import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class SsrOption_New(_option.SsrOption_, keyword='new'):
    """
    Represents INP data card data option new options.

    Attributes:
        numbers: Tuple of surface numbers to start run.
    """

    _REGEX = re.compile(r'\Anew(( \S+)+)\Z')

    def __init__(self, numbers: tuple[types.Integer]):
        """
        Initializes ``SsrOption_New``.

        Parameters:
            numbers: Tuple of surface numbers to start run.

        Returns:
            ``SsrOption_New``.

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
        Generates ``SsrOption_New`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``SsrOption_New``.

        Raises:
            InpError: SYNTAX_SSR_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SsrOption_New._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        numbers = types._Tuple(
            [types.Integer.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[1])]
        )

        return SsrOption_New(numbers)
