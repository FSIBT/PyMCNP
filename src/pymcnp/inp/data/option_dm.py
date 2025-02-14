import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Dm(_option.DataOption_, keyword='dm'):
    """
    Represents INP data card dm options.

    Attributes:
        zaids: Tuple of ZAID aliases.
    """

    _REGEX = re.compile(r'\Adm(( \S+)+)\Z')

    def __init__(self, zaids: tuple[types.Zaid]):
        """
        Initializes ``DataOption_Dm``.

        Parameters:
            zaids: Tuple of ZAID aliases.

        Returns:
            ``DataOption_Dm``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if zaids is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, zaids)

        self.value: typing.Final[tuple[any]] = types._Tuple([zaids])
        self.zaids: typing.Final[tuple[types.Zaid]] = zaids

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Dm`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Dm``.

        Raises:
            McnpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Dm._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_DATA_OPTION, source)

        zaids = types._Tuple(
            [types.Zaid.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[1])]
        )

        return DataOption_Dm(zaids)
