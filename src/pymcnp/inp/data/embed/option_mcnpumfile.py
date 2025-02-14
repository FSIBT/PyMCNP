import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class EmbedOption_Mcnpumfile(_option.EmbedOption_, keyword='mcnpumfile'):
    """
    Represents INP data card data option mcnpumfile options.

    Attributes:
        filename: Name of the MCNPUM output file.
    """

    _REGEX = re.compile(r'\Amcnpumfile( \S+)\Z')

    def __init__(self, filename: types.String):
        """
        Initializes ``EmbedOption_Mcnpumfile``.

        Parameters:
            filename: Name of the MCNPUM output file.

        Returns:
            ``EmbedOption_Mcnpumfile``.

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
        Generates ``EmbedOption_Mcnpumfile`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``EmbedOption_Mcnpumfile``.

        Raises:
            McnpError: SYNTAX_EMBED_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = EmbedOption_Mcnpumfile._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_EMBED_OPTION, source)

        filename = types.String.from_mcnp(tokens[1])

        return EmbedOption_Mcnpumfile(filename)
