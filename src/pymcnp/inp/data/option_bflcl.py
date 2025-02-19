import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Bflcl(_option.DataOption_, keyword='bflcl'):
    """
    Represents INP data card bflcl options.

    Attributes:
        numbers: Tuple of BFLD map numbers.
    """

    _REGEX = re.compile(r'\Abflcl(( \S+)+)\Z')

    def __init__(self, numbers: tuple[types.Integer]):
        """
        Initializes ``DataOption_Bflcl``.

        Parameters:
            numbers: Tuple of BFLD map numbers.

        Returns:
            ``DataOption_Bflcl``.

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
        Generates ``DataOption_Bflcl`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Bflcl``.

        Raises:
            InpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Bflcl._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        numbers = types._Tuple(
            [types.Integer.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[1])]
        )

        return DataOption_Bflcl(numbers)
