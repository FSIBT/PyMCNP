import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class SdefOption_Ccc(_option.SdefOption_, keyword='ccc'):
    """
    Represents INP data card data option ccc options.

    Attributes:
        number: Cookie-cutter cell number.
    """

    _REGEX = re.compile(r'\Accc( \S+)\Z')

    def __init__(self, number: types.Integer):
        """
        Initializes ``SdefOption_Ccc``.

        Parameters:
            number: Cookie-cutter cell number.

        Returns:
            ``SdefOption_Ccc``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if number is None or not (0 <= number <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, number)

        self.value: typing.Final[tuple[any]] = types._Tuple([number])
        self.number: typing.Final[types.Integer] = number

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SdefOption_Ccc`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``SdefOption_Ccc``.

        Raises:
            InpError: SYNTAX_SDEF_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SdefOption_Ccc._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        number = types.Integer.from_mcnp(tokens[1])

        return SdefOption_Ccc(number)
