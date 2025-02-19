import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class EmbedOption_Meeout(_option.EmbedOption_, keyword='meeout'):
    """
    Represents INP data card data option meeout options.

    Attributes:
        filename: Name assigned to EEOUT, the elemental edit output file.
    """

    _REGEX = re.compile(r'\Ameeout( \S+)\Z')

    def __init__(self, filename: types.String):
        """
        Initializes ``EmbedOption_Meeout``.

        Parameters:
            filename: Name assigned to EEOUT, the elemental edit output file.

        Returns:
            ``EmbedOption_Meeout``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if filename is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, filename)

        self.value: typing.Final[tuple[any]] = types._Tuple([filename])
        self.filename: typing.Final[types.String] = filename

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``EmbedOption_Meeout`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``EmbedOption_Meeout``.

        Raises:
            InpError: SYNTAX_EMBED_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = EmbedOption_Meeout._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        filename = types.String.from_mcnp(tokens[1])

        return EmbedOption_Meeout(filename)
