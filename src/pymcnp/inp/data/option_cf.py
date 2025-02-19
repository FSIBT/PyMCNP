import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Cf(_option.DataOption_, keyword='cf'):
    """
    Represents INP data card cf options.

    Attributes:
        numbers: Tallies for problem cell numbers to flag.
        suffix: Data card option suffix.
    """

    _REGEX = re.compile(r'\Acf(\d+?)(( \S+)+)\Z')

    def __init__(self, numbers: tuple[types.Integer], suffix: types.Integer):
        """
        Initializes ``DataOption_Cf``.

        Parameters:
            numbers: Tallies for problem cell numbers to flag.
            suffix: Data card option suffix.

        Returns:
            ``DataOption_Cf``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if numbers is None or not (filter(lambda entry: not (0 <= entry <= 99_999_999), numbers)):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, numbers)
        if suffix is None or not (suffix <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)

        self.value: typing.Final[tuple[any]] = types._Tuple([numbers])
        self.numbers: typing.Final[tuple[types.Integer]] = numbers
        self.suffix: typing.Final[types.Integer] = suffix

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Cf`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Cf``.

        Raises:
            InpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Cf._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        suffix = types.Integer.from_mcnp(tokens[1])
        numbers = types._Tuple(
            [types.Integer.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[2])]
        )

        return DataOption_Cf(numbers, suffix)
