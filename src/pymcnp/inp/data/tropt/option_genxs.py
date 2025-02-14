import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class TroptOption_Genxs(_option.TroptOption_, keyword='genxs'):
    """
    Represents INP data card data option genxs options.

    Attributes:
        filename: Cross section generation setting.
    """

    _REGEX = re.compile(r'\Agenxs( \S+)\Z')

    def __init__(self, filename: types.String):
        """
        Initializes ``TroptOption_Genxs``.

        Parameters:
            filename: Cross section generation setting.

        Returns:
            ``TroptOption_Genxs``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if filename is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, filename)

        self.value: typing.Final[tuple[any]] = types._Tuple([filename])
        self.filename: typing.Final[types.String] = filename

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``TroptOption_Genxs`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``TroptOption_Genxs``.

        Raises:
            McnpError: SYNTAX_TROPT_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = TroptOption_Genxs._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_TROPT_OPTION, source)

        filename = types.String.from_mcnp(tokens[1])

        return TroptOption_Genxs(filename)
