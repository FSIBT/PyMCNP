import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class EmbeeOption_Embed(_option.EmbeeOption_, keyword='embed'):
    """
    Represents INP data card data option embed options.

    Attributes:
        number: Embedded mesh universe number.
    """

    _REGEX = re.compile(r'\Aembed( \S+)\Z')

    def __init__(self, number: types.Integer):
        """
        Initializes ``EmbeeOption_Embed``.

        Parameters:
            number: Embedded mesh universe number.

        Returns:
            ``EmbeeOption_Embed``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if number is None or not (0 <= number <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, number)

        self.value: typing.Final[tuple[any]] = types._Tuple([number])
        self.number: typing.Final[types.Integer] = number

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``EmbeeOption_Embed`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``EmbeeOption_Embed``.

        Raises:
            InpError: SYNTAX_EMBEE_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = EmbeeOption_Embed._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        number = types.Integer.from_mcnp(tokens[1])

        return EmbeeOption_Embed(number)
