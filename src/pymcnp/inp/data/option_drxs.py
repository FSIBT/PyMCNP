import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Drxs(_option.DataOption_, keyword='drxs'):
    """
    Represents INP data card drxs options.

    Attributes:
        zaids: Tuple of ZAID aliases.
    """

    _REGEX = re.compile(r'\Adrxs(( \S+)+)?\Z')

    def __init__(self, zaids: tuple[types.Zaid] = None):
        """
        Initializes ``DataOption_Drxs``.

        Parameters:
            zaids: Tuple of ZAID aliases.

        Returns:
            ``DataOption_Drxs``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        self.value: typing.Final[tuple[any]] = types._Tuple([zaids])
        self.zaids: typing.Final[tuple[types.Zaid]] = zaids

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Drxs`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Drxs``.

        Raises:
            InpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Drxs._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        zaids = (
            types._Tuple(
                [types.Zaid.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[1])]
            )
            if tokens[1]
            else None
        )

        return DataOption_Drxs(zaids)
