import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class EmbeeOption_Mat(_option.EmbeeOption_, keyword='mat'):
    """
    Represents INP data card data option mat options.

    Attributes:
        number: Material number.
    """

    _REGEX = re.compile(r'\Amat( \S+)\Z')

    def __init__(self, number: types.Integer):
        """
        Initializes ``EmbeeOption_Mat``.

        Parameters:
            number: Material number.

        Returns:
            ``EmbeeOption_Mat``.

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
        Generates ``EmbeeOption_Mat`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``EmbeeOption_Mat``.

        Raises:
            InpError: SYNTAX_EMBEE_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = EmbeeOption_Mat._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        number = types.Integer.from_mcnp(tokens[1])

        return EmbeeOption_Mat(number)
