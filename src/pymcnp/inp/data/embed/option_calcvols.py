import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class EmbedOption_Calcvols(_option.EmbedOption_, keyword='calcvols'):
    """
    Represents INP data card data option calcvols options.

    Attributes:
        setting: Yes/no calculate the inferred geometry cell information.
    """

    _REGEX = re.compile(r'\Acalcvols( \S+)\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``EmbedOption_Calcvols``.

        Parameters:
            setting: Yes/no calculate the inferred geometry cell information.

        Returns:
            ``EmbedOption_Calcvols``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if setting is None or setting not in {'yes', 'no'}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, setting)

        self.value: typing.Final[tuple[any]] = types._Tuple([setting])
        self.setting: typing.Final[types.String] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``EmbedOption_Calcvols`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``EmbedOption_Calcvols``.

        Raises:
            McnpError: SYNTAX_EMBED_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = EmbedOption_Calcvols._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_EMBED_OPTION, source)

        setting = types.String.from_mcnp(tokens[1])

        return EmbedOption_Calcvols(setting)
