import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class CellOption_Imp(_option.CellOption_, keyword='imp'):
    """
    Represents INP cell card imp options.

    Attributes:
        importance: Cell particle importance.
        designator: Particle designator.
    """

    _REGEX = re.compile(r'\Aimp:(\S+?)( \S+)\Z')

    def __init__(self, importance: types.Real, designator: types.Designator):
        """
        Initializes ``CellOption_Imp``.

        Parameters:
            importance: Cell particle importance.
            designator: Particle designator.

        Returns:
            ``CellOption_Imp``.

        Raises:
            McnpError: SEMANTICS_CELL_OPTION_VALUE.
            McnpError: SEMANTICS_CELL_OPTION_DESIGNATOR.
        """

        if importance is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_CELL_OPTION_VALUE, importance)
        if designator is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_CELL_OPTION_DESIGNATOR, designator)

        self.value: typing.Final[tuple[any]] = types._Tuple([importance])
        self.importance: typing.Final[types.Real] = importance
        self.designator: typing.Final[types.Designator] = designator

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``CellOption_Imp`` from INP.

        Parameters:
            source: INP cell card option.

        Returns:
            ``CellOption_Imp``.

        Raises:
            McnpError: SYNTAX_CELL_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = CellOption_Imp._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_CELL_OPTION, source)

        designator = types.Designator.from_mcnp(tokens[1])
        importance = types.Real.from_mcnp(tokens[2])

        return CellOption_Imp(importance, designator)
