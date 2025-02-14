import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class SdefOption_Cel(_option.SdefOption_, keyword='cel'):
    """
    Represents INP data card data option cel options.

    Attributes:
        number: Cell number.
    """

    _REGEX = re.compile(r'\Acel( \S+)\Z')

    def __init__(self, number: types.Integer):
        """
        Initializes ``SdefOption_Cel``.

        Parameters:
            number: Cell number.

        Returns:
            ``SdefOption_Cel``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if number is None or not (0 <= number <= 99_999_999):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, number)

        self.value: typing.Final[tuple[any]] = types._Tuple([number])
        self.number: typing.Final[types.Integer] = number

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SdefOption_Cel`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``SdefOption_Cel``.

        Raises:
            McnpError: SYNTAX_SDEF_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SdefOption_Cel._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_SDEF_OPTION, source)

        number = types.Integer.from_mcnp(tokens[1])

        return SdefOption_Cel(number)
