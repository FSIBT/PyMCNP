import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class CellOption_Ext(_option.CellOption_, keyword='ext'):
    """
    Represents INP cell card ext options.

    Attributes:
        stretch: Cell exponential transform stretching specifier.
        designator: Cell particle designator.
    """

    _REGEX = re.compile(r'\Aext:(\S+?)( \S+)\Z')

    def __init__(self, stretch: str, designator: types.Designator):
        """
        Initializes ``CellOption_Ext``.

        Parameters:
            stretch: Cell exponential transform stretching specifier.
            designator: Cell particle designator.

        Returns:
            ``CellOption_Ext``.

        Raises:
            McnpError: SEMANTICS_CELL_OPTION_VALUE.
            McnpError: SEMANTICS_CELL_OPTION_DESIGNATOR.
        """

        if stretch is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_CELL_OPTION_VALUE, stretch)
        if designator is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_CELL_OPTION_DESIGNATOR, designator)

        self.value: typing.Final[tuple[any]] = types._Tuple([stretch])
        self.stretch: typing.Final[str] = stretch
        self.designator: typing.Final[types.Designator] = designator

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``CellOption_Ext`` from INP.

        Parameters:
            source: INP cell card option.

        Returns:
            ``CellOption_Ext``.

        Raises:
            McnpError: SYNTAX_CELL_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = CellOption_Ext._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_CELL_OPTION, source)

        designator = types.Designator.from_mcnp(tokens[1])
        stretch = str.from_mcnp(tokens[2])

        return CellOption_Ext(stretch, designator)
