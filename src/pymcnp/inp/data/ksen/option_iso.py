import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class KsenOption_Iso(_option.KsenOption_, keyword='iso'):
    """
    Represents INP data card data option iso options.

    Attributes:
        zaids: List of ZAIDs for pertubation.
    """

    _REGEX = re.compile(r'\Aiso(( \S+)+)\Z')

    def __init__(self, zaids: tuple[types.Real]):
        """
        Initializes ``KsenOption_Iso``.

        Parameters:
            zaids: List of ZAIDs for pertubation.

        Returns:
            ``KsenOption_Iso``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if zaids is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, zaids)

        self.value: typing.Final[tuple[any]] = types._Tuple([zaids])
        self.zaids: typing.Final[tuple[types.Real]] = zaids

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``KsenOption_Iso`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``KsenOption_Iso``.

        Raises:
            McnpError: SYNTAX_KSEN_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = KsenOption_Iso._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_KSEN_OPTION, source)

        zaids = types._Tuple(
            [types.Real.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[1])]
        )

        return KsenOption_Iso(zaids)
