import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Ext(_option.DataOption_, keyword='ext'):
    """
    Represents INP data card ext options.

    Attributes:
        stretching: Stretching direction for the cell.
        designator: Data card particle designator.
    """

    _REGEX = re.compile(r'\Aext:(\S+?)(( \S+)+)\Z')

    def __init__(self, stretching: tuple[types.Real], designator: types.Designator):
        """
        Initializes ``DataOption_Ext``.

        Parameters:
            stretching: Stretching direction for the cell.
            designator: Data card particle designator.

        Returns:
            ``DataOption_Ext``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_DESIGNATOR.
        """

        if stretching is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, stretching)
        if designator is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_DESIGNATOR, designator)

        self.value: typing.Final[tuple[any]] = types._Tuple([stretching])
        self.stretching: typing.Final[tuple[types.Real]] = stretching
        self.designator: typing.Final[types.Designator] = designator

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Ext`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Ext``.

        Raises:
            McnpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Ext._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_DATA_OPTION, source)

        designator = types.Designator.from_mcnp(tokens[1])
        stretching = types._Tuple(
            [types.Real.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[2])]
        )

        return DataOption_Ext(stretching, designator)
