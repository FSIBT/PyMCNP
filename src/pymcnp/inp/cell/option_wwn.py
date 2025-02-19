import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class CellOption_Wwn(_option.CellOption_, keyword='wwn'):
    """
    Represents INP cell card wwn options.

    Attributes:
        bound: Cell weight-window space, time, or energy lower bound.
        suffix: Cell option suffix.
        designator: Cell particle designator.
    """

    _REGEX = re.compile(r'\Awwn(\d+?):(\S+?)( \S+)\Z')

    def __init__(self, bound: types.Real, suffix: types.Integer, designator: types.Designator):
        """
        Initializes ``CellOption_Wwn``.

        Parameters:
            bound: Cell weight-window space, time, or energy lower bound.
            suffix: Cell option suffix.
            designator: Cell particle designator.

        Returns:
            ``CellOption_Wwn``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if bound is None or not (bound == -1 or bound >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bound)
        if suffix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, designator)

        self.value: typing.Final[tuple[any]] = types._Tuple([bound])
        self.bound: typing.Final[types.Real] = bound
        self.suffix: typing.Final[types.Integer] = suffix
        self.designator: typing.Final[types.Designator] = designator

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``CellOption_Wwn`` from INP.

        Parameters:
            source: INP cell card option.

        Returns:
            ``CellOption_Wwn``.

        Raises:
            InpError: SYNTAX_CELL_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = CellOption_Wwn._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        suffix = types.Integer.from_mcnp(tokens[1])
        designator = types.Designator.from_mcnp(tokens[2])
        bound = types.Real.from_mcnp(tokens[3])

        return CellOption_Wwn(bound, suffix, designator)
