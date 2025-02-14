import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class SsrOption_Old(_option.SsrOption_, keyword='old'):
    """
    Represents INP data card data option old options.

    Attributes:
        numbers: Tuple of surface numbers from subset of surfaces on SSW card.
    """

    _REGEX = re.compile(r'\Aold(( \S+)+)\Z')

    def __init__(self, numbers: tuple[types.Integer]):
        """
        Initializes ``SsrOption_Old``.

        Parameters:
            numbers: Tuple of surface numbers from subset of surfaces on SSW card.

        Returns:
            ``SsrOption_Old``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if numbers is None or not (filter(lambda entry: not (1 <= entry <= 99_999_999), numbers)):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, numbers)

        self.value: typing.Final[tuple[any]] = types._Tuple([numbers])
        self.numbers: typing.Final[tuple[types.Integer]] = numbers

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SsrOption_Old`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``SsrOption_Old``.

        Raises:
            McnpError: SYNTAX_SSR_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SsrOption_Old._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_SSR_OPTION, source)

        numbers = types._Tuple(
            [types.Integer.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[1])]
        )

        return SsrOption_Old(numbers)
