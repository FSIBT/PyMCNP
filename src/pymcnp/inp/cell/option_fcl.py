import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class CellOption_Fcl(_option.CellOption_, keyword='fcl'):
    """
    Represents INP cell card fcl options.

    Attributes:
        control: Cell forced-collision control.
        designator: Cell particle designator.
    """

    _REGEX = re.compile(r'\Afcl:(\S+?)( \S+)\Z')

    def __init__(self, control: types.Real, designator: types.Designator):
        """
        Initializes ``CellOption_Fcl``.

        Parameters:
            control: Cell forced-collision control.
            designator: Cell particle designator.

        Returns:
            ``CellOption_Fcl``.

        Raises:
            McnpError: SEMANTICS_CELL_OPTION_VALUE.
            McnpError: SEMANTICS_CELL_OPTION_DESIGNATOR.
        """

        if control is None or not (-1 <= control <= 1):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_CELL_OPTION_VALUE, control)
        if designator is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_CELL_OPTION_DESIGNATOR, designator)

        self.value: typing.Final[tuple[any]] = types._Tuple([control])
        self.control: typing.Final[types.Real] = control
        self.designator: typing.Final[types.Designator] = designator

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``CellOption_Fcl`` from INP.

        Parameters:
            source: INP cell card option.

        Returns:
            ``CellOption_Fcl``.

        Raises:
            McnpError: SYNTAX_CELL_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = CellOption_Fcl._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_CELL_OPTION, source)

        designator = types.Designator.from_mcnp(tokens[1])
        control = types.Real.from_mcnp(tokens[2])

        return CellOption_Fcl(control, designator)
