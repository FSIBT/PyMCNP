import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class EmbedOption_Debug(_option.EmbedOption_, keyword='debug'):
    """
    Represents INP data card data option debug options.

    Attributes:
        parameter: Debug parameter.
    """

    _REGEX = re.compile(r'\Adebug( \S+)\Z')

    def __init__(self, parameter: types.String):
        """
        Initializes ``EmbedOption_Debug``.

        Parameters:
            parameter: Debug parameter.

        Returns:
            ``EmbedOption_Debug``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if parameter is None or parameter not in {'echomesh'}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, parameter)

        self.value: typing.Final[tuple[any]] = types._Tuple([parameter])
        self.parameter: typing.Final[types.String] = parameter

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``EmbedOption_Debug`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``EmbedOption_Debug``.

        Raises:
            McnpError: SYNTAX_EMBED_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = EmbedOption_Debug._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_EMBED_OPTION, source)

        parameter = types.String.from_mcnp(tokens[1])

        return EmbedOption_Debug(parameter)
