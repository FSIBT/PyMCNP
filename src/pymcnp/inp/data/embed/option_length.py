import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class EmbedOption_Length(_option.EmbedOption_, keyword='length'):
    """
    Represents INP data card data option length options.

    Attributes:
        factor: Conversion factor to centimeters for all mesh dimentions.
    """

    _REGEX = re.compile(r'\Alength( \S+)\Z')

    def __init__(self, factor: types.Real):
        """
        Initializes ``EmbedOption_Length``.

        Parameters:
            factor: Conversion factor to centimeters for all mesh dimentions.

        Returns:
            ``EmbedOption_Length``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if factor is None or not (factor > 0):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, factor)

        self.value: typing.Final[tuple[any]] = types._Tuple([factor])
        self.factor: typing.Final[types.Real] = factor

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``EmbedOption_Length`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``EmbedOption_Length``.

        Raises:
            McnpError: SYNTAX_EMBED_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = EmbedOption_Length._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_EMBED_OPTION, source)

        factor = types.Real.from_mcnp(tokens[1])

        return EmbedOption_Length(factor)
