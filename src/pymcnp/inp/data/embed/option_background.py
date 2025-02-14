import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class EmbedOption_Background(_option.EmbedOption_, keyword='background'):
    """
    Represents INP data card data option background options.

    Attributes:
        number: Background pseudo-cell number.
    """

    _REGEX = re.compile(r'\Abackground( \S+)\Z')

    def __init__(self, number: types.Integer):
        """
        Initializes ``EmbedOption_Background``.

        Parameters:
            number: Background pseudo-cell number.

        Returns:
            ``EmbedOption_Background``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if number is None or not (1 <= number <= 99_999_999):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, number)

        self.value: typing.Final[tuple[any]] = types._Tuple([number])
        self.number: typing.Final[types.Integer] = number

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``EmbedOption_Background`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``EmbedOption_Background``.

        Raises:
            McnpError: SYNTAX_EMBED_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = EmbedOption_Background._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_EMBED_OPTION, source)

        number = types.Integer.from_mcnp(tokens[1])

        return EmbedOption_Background(number)
