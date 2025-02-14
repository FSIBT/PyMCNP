import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class KpertOption_Iso(_option.KpertOption_, keyword='iso'):
    """
    Represents INP data card data option iso options.

    Attributes:
        zaids: List of ZAIDs for pertubation.
    """

    _REGEX = re.compile(r'\Aiso(( \S+)+)\Z')

    def __init__(self, zaids: tuple[types.Real]):
        """
        Initializes ``KpertOption_Iso``.

        Parameters:
            zaids: List of ZAIDs for pertubation.

        Returns:
            ``KpertOption_Iso``.

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
        Generates ``KpertOption_Iso`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``KpertOption_Iso``.

        Raises:
            McnpError: SYNTAX_KPERT_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = KpertOption_Iso._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_KPERT_OPTION, source)

        zaids = types._Tuple(
            [types.Real.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[1])]
        )

        return KpertOption_Iso(zaids)
