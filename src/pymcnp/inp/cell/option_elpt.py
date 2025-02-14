import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class CellOption_Elpt(_option.CellOption_, keyword='elpt'):
    """
    Represents INP cell card elpt options.

    Attributes:
        cutoff: Cell energy cutoff.
        designator: Cell particle designator.
    """

    _REGEX = re.compile(r'\Aelpt:(\S+?)( \S+)\Z')

    def __init__(self, cutoff: types.Real, designator: types.Designator):
        """
        Initializes ``CellOption_Elpt``.

        Parameters:
            cutoff: Cell energy cutoff.
            designator: Cell particle designator.

        Returns:
            ``CellOption_Elpt``.

        Raises:
            McnpError: SEMANTICS_CELL_OPTION_VALUE.
            McnpError: SEMANTICS_CELL_OPTION_DESIGNATOR.
        """

        if cutoff is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_CELL_OPTION_VALUE, cutoff)
        if designator is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_CELL_OPTION_DESIGNATOR, designator)

        self.value: typing.Final[tuple[any]] = types._Tuple([cutoff])
        self.cutoff: typing.Final[types.Real] = cutoff
        self.designator: typing.Final[types.Designator] = designator

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``CellOption_Elpt`` from INP.

        Parameters:
            source: INP cell card option.

        Returns:
            ``CellOption_Elpt``.

        Raises:
            McnpError: SYNTAX_CELL_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = CellOption_Elpt._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_CELL_OPTION, source)

        designator = types.Designator.from_mcnp(tokens[1])
        cutoff = types.Real.from_mcnp(tokens[2])

        return CellOption_Elpt(cutoff, designator)
