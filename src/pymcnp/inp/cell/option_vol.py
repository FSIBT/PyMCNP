import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class CellOption_Vol(_option.CellOption_, keyword='vol'):
    """
    Represents INP cell card vol options.

    Attributes:
        volume: Cell volume.
    """

    _REGEX = re.compile(r'\Avol( \S+)\Z')

    def __init__(self, volume: types.Real):
        """
        Initializes ``CellOption_Vol``.

        Parameters:
            volume: Cell volume.

        Returns:
            ``CellOption_Vol``.

        Raises:
            McnpError: SEMANTICS_CELL_OPTION_VALUE.
        """

        if volume is None or not (volume >= 0):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_CELL_OPTION_VALUE, volume)

        self.value: typing.Final[tuple[any]] = types._Tuple([volume])
        self.volume: typing.Final[types.Real] = volume

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``CellOption_Vol`` from INP.

        Parameters:
            source: INP cell card option.

        Returns:
            ``CellOption_Vol``.

        Raises:
            McnpError: SYNTAX_CELL_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = CellOption_Vol._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_CELL_OPTION, source)

        volume = types.Real.from_mcnp(tokens[1])

        return CellOption_Vol(volume)
