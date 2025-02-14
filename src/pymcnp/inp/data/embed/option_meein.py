import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class EmbedOption_Meein(_option.EmbedOption_, keyword='meein'):
    """
    Represents INP data card data option meein options.

    Attributes:
        filename: Name of the EEOUT results file to read.
    """

    _REGEX = re.compile(r'\Ameein( \S+)\Z')

    def __init__(self, filename: types.String):
        """
        Initializes ``EmbedOption_Meein``.

        Parameters:
            filename: Name of the EEOUT results file to read.

        Returns:
            ``EmbedOption_Meein``.

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
        Generates ``EmbedOption_Meein`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``EmbedOption_Meein``.

        Raises:
            McnpError: SYNTAX_EMBED_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = EmbedOption_Meein._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_EMBED_OPTION, source)

        filename = types.String.from_mcnp(tokens[1])

        return EmbedOption_Meein(filename)
