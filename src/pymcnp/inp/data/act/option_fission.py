import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class ActOption_Fission(_option.ActOption_, keyword='fission'):
    """
    Represents INP data card data option fission options.

    Attributes:
        kind: Type of delayed particle(s) to be produced from residuals created by fission.
    """

    _REGEX = re.compile(r'\Afission( \S+)\Z')

    def __init__(self, kind: types.String):
        """
        Initializes ``ActOption_Fission``.

        Parameters:
            kind: Type of delayed particle(s) to be produced from residuals created by fission.

        Returns:
            ``ActOption_Fission``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if kind is None or type not in {'none', 'n,p,e,f,a', 'all'}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, kind)

        self.value: typing.Final[tuple[any]] = types._Tuple([kind])
        self.kind: typing.Final[types.String] = kind

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``ActOption_Fission`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``ActOption_Fission``.

        Raises:
            McnpError: SYNTAX_ACT_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = ActOption_Fission._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_ACT_OPTION, source)

        kind = types.String.from_mcnp(tokens[1])

        return ActOption_Fission(kind)
