import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class EmbedOption_Mgeoin(_option.EmbedOption_, keyword='mgeoin'):
    """
    Represents INP data card data option mgeoin options.

    Attributes:
        filename: Name of the input file containing the mesh description.
    """

    _REGEX = re.compile(r'\Amgeoin( \S+)\Z')

    def __init__(self, filename: types.String):
        """
        Initializes ``EmbedOption_Mgeoin``.

        Parameters:
            filename: Name of the input file containing the mesh description.

        Returns:
            ``EmbedOption_Mgeoin``.

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
        Generates ``EmbedOption_Mgeoin`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``EmbedOption_Mgeoin``.

        Raises:
            McnpError: SYNTAX_EMBED_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = EmbedOption_Mgeoin._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_EMBED_OPTION, source)

        filename = types.String.from_mcnp(tokens[1])

        return EmbedOption_Mgeoin(filename)
