import re
import typing

from . import _option
from .....utils import types
from .....utils import errors
from .....utils import _parser


class BlockOption_Trcor(_option.BlockOption_, keyword='trcor'):
    """
    Represents INP data card data option dawwg option trcor options.

    Attributes:
        setting: Trcor.
    """

    _REGEX = re.compile(r'\Atrcor( \S+)\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``BlockOption_Trcor``.

        Parameters:
            setting: Trcor.

        Returns:
            ``BlockOption_Trcor``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if setting is None or setting not in {'diag'}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, setting)

        self.value: typing.Final[tuple[any]] = types._Tuple([setting])
        self.setting: typing.Final[types.String] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``BlockOption_Trcor`` from INP.

        Parameters:
            source: INP data card data option dawwg option option.

        Returns:
            ``BlockOption_Trcor``.

        Raises:
            McnpError: SYNTAX_BLOCK_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = BlockOption_Trcor._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_BLOCK_OPTION, source)

        setting = types.String.from_mcnp(tokens[1])

        return BlockOption_Trcor(setting)
