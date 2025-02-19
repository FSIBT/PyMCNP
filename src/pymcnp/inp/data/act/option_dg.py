import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class ActOption_Dg(_option.ActOption_, keyword='dg'):
    """
    Represents INP data card data option dg options.

    Attributes:
        source: Delayed gamma data source.
    """

    _REGEX = re.compile(r'\Adg( \S+)\Z')

    def __init__(self, source: types.String):
        """
        Initializes ``ActOption_Dg``.

        Parameters:
            source: Delayed gamma data source.

        Returns:
            ``ActOption_Dg``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if source is None or source not in {'line', 'mg', 'none'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, source)

        self.value: typing.Final[tuple[any]] = types._Tuple([source])
        self.source: typing.Final[types.String] = source

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``ActOption_Dg`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``ActOption_Dg``.

        Raises:
            InpError: SYNTAX_ACT_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = ActOption_Dg._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        source = types.String.from_mcnp(tokens[1])

        return ActOption_Dg(source)
