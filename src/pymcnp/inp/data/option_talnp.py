import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Talnp(_option.DataOption_, keyword='talnp'):
    """
    Represents INP data card talnp options.

    Attributes:
        tallies: Tallies to exclude from output.
    """

    _REGEX = re.compile(r'\Atalnp(( \S+)+)?\Z')

    def __init__(self, tallies: tuple[types.Integer] = None):
        """
        Initializes ``DataOption_Talnp``.

        Parameters:
            tallies: Tallies to exclude from output.

        Returns:
            ``DataOption_Talnp``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if tallies is not None and not (
            filter(lambda entry: not (1 <= entry <= 99_999_999), tallies)
        ):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, tallies)

        self.value: typing.Final[tuple[any]] = types._Tuple([tallies])
        self.tallies: typing.Final[tuple[types.Integer]] = tallies

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Talnp`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Talnp``.

        Raises:
            McnpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Talnp._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_DATA_OPTION, source)

        tallies = (
            types._Tuple(
                [types.Integer.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[1])]
            )
            if tokens[1]
            else None
        )

        return DataOption_Talnp(tallies)
