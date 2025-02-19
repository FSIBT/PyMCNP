import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class ActOption_Nap(_option.ActOption_, keyword='nap'):
    """
    Represents INP data card data option nap options.

    Attributes:
        count: Number of activation products.
    """

    _REGEX = re.compile(r'\Anap( \S+)\Z')

    def __init__(self, count: types.Integer):
        """
        Initializes ``ActOption_Nap``.

        Parameters:
            count: Number of activation products.

        Returns:
            ``ActOption_Nap``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if count is None or not (0 <= count):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, count)

        self.value: typing.Final[tuple[any]] = types._Tuple([count])
        self.count: typing.Final[types.Integer] = count

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``ActOption_Nap`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``ActOption_Nap``.

        Raises:
            InpError: SYNTAX_ACT_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = ActOption_Nap._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        count = types.Integer.from_mcnp(tokens[1])

        return ActOption_Nap(count)
