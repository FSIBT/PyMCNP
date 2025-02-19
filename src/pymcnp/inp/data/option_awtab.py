import re
import typing

from . import awtab
from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Awtab(_option.DataOption_, keyword='awtab'):
    """
    Represents INP data card awtab options.

    Attributes:
        weight_ratios: Tuple of atomic weight ratios.
    """

    _REGEX = re.compile(r'\Aawtab((( \S+)( \S+))+)\Z')

    def __init__(self, weight_ratios: tuple[awtab.AwtabEntry_Substance]):
        """
        Initializes ``DataOption_Awtab``.

        Parameters:
            weight_ratios: Tuple of atomic weight ratios.

        Returns:
            ``DataOption_Awtab``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if weight_ratios is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, weight_ratios)

        self.value: typing.Final[tuple[any]] = types._Tuple([weight_ratios])
        self.weight_ratios: typing.Final[tuple[awtab.AwtabEntry_Substance]] = weight_ratios

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Awtab`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Awtab``.

        Raises:
            InpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Awtab._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        weight_ratios = types._Tuple(
            [
                awtab.AwtabEntry_Substance.from_mcnp(token[0])
                for token in awtab.AwtabEntry_Substance._REGEX.finditer(tokens[1])
            ]
        )

        return DataOption_Awtab(weight_ratios)
