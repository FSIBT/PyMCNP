import re
import typing

from . import _option
from .....utils import types
from .....utils import errors
from .....utils import _parser


class BlockOption_Ngroup(_option.BlockOption_, keyword='ngroup'):
    """
    Represents INP data card data option dawwg option ngroup options.

    Attributes:
        value: Number of energy groups.
    """

    _REGEX = re.compile(r'\Angroup( \S+)\Z')

    def __init__(self, value: types.Integer):
        """
        Initializes ``BlockOption_Ngroup``.

        Parameters:
            value: Number of energy groups.

        Returns:
            ``BlockOption_Ngroup``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if value is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, value)

        self.value: typing.Final[tuple[any]] = types._Tuple([value])
        self.value: typing.Final[types.Integer] = value

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``BlockOption_Ngroup`` from INP.

        Parameters:
            source: INP data card data option dawwg option option.

        Returns:
            ``BlockOption_Ngroup``.

        Raises:
            McnpError: SYNTAX_BLOCK_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = BlockOption_Ngroup._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_BLOCK_OPTION, source)

        value = types.Integer.from_mcnp(tokens[1])

        return BlockOption_Ngroup(value)
