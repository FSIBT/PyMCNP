import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class KsenOption_Mt(_option.KsenOption_, keyword='mt'):
    """
    Represents INP data card data option mt options.

    Attributes:
        numbers: List of reaction numbers for pertubation.
    """

    _REGEX = re.compile(r'\Amt(( \S+)+)\Z')

    def __init__(self, numbers: tuple[types.Integer]):
        """
        Initializes ``KsenOption_Mt``.

        Parameters:
            numbers: List of reaction numbers for pertubation.

        Returns:
            ``KsenOption_Mt``.

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
        Generates ``KsenOption_Mt`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``KsenOption_Mt``.

        Raises:
            McnpError: SYNTAX_KSEN_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = KsenOption_Mt._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_KSEN_OPTION, source)

        numbers = types._Tuple(
            [types.Integer.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[1])]
        )

        return KsenOption_Mt(numbers)
