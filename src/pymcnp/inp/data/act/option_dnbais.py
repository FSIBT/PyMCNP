import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class ActOption_Dnbais(_option.ActOption_, keyword='dnbais'):
    """
    Represents INP data card data option dnbais options.

    Attributes:
        count: Maximum number of neutrons generated per reaction.
    """

    _REGEX = re.compile(r'\Adnbais( \S+)\Z')

    def __init__(self, count: types.Integer):
        """
        Initializes ``ActOption_Dnbais``.

        Parameters:
            count: Maximum number of neutrons generated per reaction.

        Returns:
            ``ActOption_Dnbais``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if count is None or not (0 <= count <= 10):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, count)

        self.value: typing.Final[tuple[any]] = types._Tuple([count])
        self.count: typing.Final[types.Integer] = count

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``ActOption_Dnbais`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``ActOption_Dnbais``.

        Raises:
            InpError: SYNTAX_ACT_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = ActOption_Dnbais._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        count = types.Integer.from_mcnp(tokens[1])

        return ActOption_Dnbais(count)
