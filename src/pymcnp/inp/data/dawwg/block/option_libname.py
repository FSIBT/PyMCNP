import re
import typing

from . import _option
from .....utils import types
from .....utils import errors
from .....utils import _parser


class BlockOption_Libname(_option.BlockOption_, keyword='libname'):
    """
    Represents INP data card data option dawwg option libname options.

    Attributes:
        setting: Cross-section file name.
    """

    _REGEX = re.compile(r'\Alibname( \S+)\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``BlockOption_Libname``.

        Parameters:
            setting: Cross-section file name.

        Returns:
            ``BlockOption_Libname``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if setting is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, setting)

        self.value: typing.Final[tuple[any]] = types._Tuple([setting])
        self.setting: typing.Final[types.String] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``BlockOption_Libname`` from INP.

        Parameters:
            source: INP data card data option dawwg option option.

        Returns:
            ``BlockOption_Libname``.

        Raises:
            McnpError: SYNTAX_BLOCK_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = BlockOption_Libname._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_BLOCK_OPTION, source)

        setting = types.String.from_mcnp(tokens[1])

        return BlockOption_Libname(setting)
