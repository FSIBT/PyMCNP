import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Otfdb(_option.DataOption_, keyword='otfdb'):
    """
    Represents INP data card otfdb options.

    Attributes:
        zaids: Identifiers for the broadening tables.
    """

    _REGEX = re.compile(r'\Aotfdb(( \S+)+)\Z')

    def __init__(self, zaids: tuple[types.Zaid]):
        """
        Initializes ``DataOption_Otfdb``.

        Parameters:
            zaids: Identifiers for the broadening tables.

        Returns:
            ``DataOption_Otfdb``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if zaids is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, zaids)

        self.value: typing.Final[tuple[any]] = types._Tuple([zaids])
        self.zaids: typing.Final[tuple[types.Zaid]] = zaids

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Otfdb`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Otfdb``.

        Raises:
            InpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Otfdb._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        zaids = types._Tuple(
            [types.Zaid.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[1])]
        )

        return DataOption_Otfdb(zaids)
