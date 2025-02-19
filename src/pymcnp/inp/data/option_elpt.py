import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Elpt(_option.DataOption_, keyword='elpt'):
    """
    Represents INP data card elpt options.

    Attributes:
        cutoffs: Tuple of cell lower energy cutoffs.
    """

    _REGEX = re.compile(r'\Aelpt(( \S+)+)\Z')

    def __init__(self, cutoffs: tuple[types.Real]):
        """
        Initializes ``DataOption_Elpt``.

        Parameters:
            cutoffs: Tuple of cell lower energy cutoffs.

        Returns:
            ``DataOption_Elpt``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if cutoffs is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, cutoffs)

        self.value: typing.Final[tuple[any]] = types._Tuple([cutoffs])
        self.cutoffs: typing.Final[tuple[types.Real]] = cutoffs

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Elpt`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Elpt``.

        Raises:
            InpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Elpt._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        cutoffs = types._Tuple(
            [types.Real.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[1])]
        )

        return DataOption_Elpt(cutoffs)
