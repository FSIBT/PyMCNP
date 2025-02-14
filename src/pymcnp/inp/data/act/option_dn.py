import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class ActOption_Dn(_option.ActOption_, keyword='dn'):
    """
    Represents INP data card data option dn options.

    Attributes:
        source: Delayed neutron data source.
    """

    _REGEX = re.compile(r'\Adn( \S+)\Z')

    def __init__(self, source: types.String):
        """
        Initializes ``ActOption_Dn``.

        Parameters:
            source: Delayed neutron data source.

        Returns:
            ``ActOption_Dn``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if source is None or source not in {'model', 'library', 'both', 'prompt'}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, source)

        self.value: typing.Final[tuple[any]] = types._Tuple([source])
        self.source: typing.Final[types.String] = source

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``ActOption_Dn`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``ActOption_Dn``.

        Raises:
            McnpError: SYNTAX_ACT_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = ActOption_Dn._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_ACT_OPTION, source)

        source = types.String.from_mcnp(tokens[1])

        return ActOption_Dn(source)
