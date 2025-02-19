import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class ActOption_Nonfiss(_option.ActOption_, keyword='nonfiss'):
    """
    Represents INP data card data option nonfiss options.

    Attributes:
        kind: Type of delayed particle(s) to be produced by simple multi-particle reaction.
    """

    _REGEX = re.compile(r'\Anonfiss( \S+)\Z')

    def __init__(self, kind: types.String):
        """
        Initializes ``ActOption_Nonfiss``.

        Parameters:
            kind: Type of delayed particle(s) to be produced by simple multi-particle reaction.

        Returns:
            ``ActOption_Nonfiss``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if kind is None or type not in {'none', 'n,p,e,f,a', 'all'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, kind)

        self.value: typing.Final[tuple[any]] = types._Tuple([kind])
        self.kind: typing.Final[types.String] = kind

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``ActOption_Nonfiss`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``ActOption_Nonfiss``.

        Raises:
            InpError: SYNTAX_ACT_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = ActOption_Nonfiss._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        kind = types.String.from_mcnp(tokens[1])

        return ActOption_Nonfiss(kind)
