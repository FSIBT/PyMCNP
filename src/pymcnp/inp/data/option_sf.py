import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Sf(_option.DataOption_, keyword='sf'):
    """
    Represents INP data card sf options.

    Attributes:
        numbers: Tallies for problem surface numbers to flag.
        suffix: Data card option suffix.
    """

    _REGEX = re.compile(r'\Asf(\d+?)(( \S+)+)\Z')

    def __init__(self, numbers: tuple[types.Integer], suffix: types.Integer):
        """
        Initializes ``DataOption_Sf``.

        Parameters:
            numbers: Tallies for problem surface numbers to flag.
            suffix: Data card option suffix.

        Returns:
            ``DataOption_Sf``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_SUFFIX.
        """

        if numbers is None or not (filter(lambda entry: not (0 <= entry <= 99_999_999), numbers)):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, numbers)
        if suffix is None or not (suffix <= 99_999_999):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_SUFFIX, suffix)

        self.value: typing.Final[tuple[any]] = types._Tuple([numbers])
        self.numbers: typing.Final[tuple[types.Integer]] = numbers
        self.suffix: typing.Final[types.Integer] = suffix

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Sf`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Sf``.

        Raises:
            McnpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Sf._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_DATA_OPTION, source)

        suffix = types.Integer.from_mcnp(tokens[1])
        numbers = types._Tuple(
            [types.Integer.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[2])]
        )

        return DataOption_Sf(numbers, suffix)
