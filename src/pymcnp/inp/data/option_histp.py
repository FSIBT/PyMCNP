import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Histp(_option.DataOption_, keyword='histp'):
    """
    Represents INP data card histp options.

    Attributes:
        lhist: Number of words written to a HISTP file.
        cells: Cell numbers.
    """

    _REGEX = re.compile(r'\Ahistp( \S+)?(( \S+)+)?\Z')

    def __init__(self, lhist: types.Integer = None, cells: tuple[types.Integer] = None):
        """
        Initializes ``DataOption_Histp``.

        Parameters:
            lhist: Number of words written to a HISTP file.
            cells: Cell numbers.

        Returns:
            ``DataOption_Histp``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        self.value: typing.Final[tuple[any]] = types._Tuple([lhist, cells])
        self.lhist: typing.Final[types.Integer] = lhist
        self.cells: typing.Final[tuple[types.Integer]] = cells

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Histp`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Histp``.

        Raises:
            InpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Histp._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        lhist = types.Integer.from_mcnp(tokens[1]) if tokens[1] else None
        cells = (
            types._Tuple(
                [types.Integer.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[2])]
            )
            if tokens[2]
            else None
        )

        return DataOption_Histp(lhist, cells)
