import re
import typing

from . import _option
from .....utils import types
from .....utils import errors
from .....utils import _parser


class BlockOption_Mt(_option.BlockOption_, keyword='mt'):
    """
    Represents INP data card data option dawwg option mt options.

    Attributes:
        setting: Number of materials.
    """

    _REGEX = re.compile(r'\Amt( \S+)\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``BlockOption_Mt``.

        Parameters:
            setting: Number of materials.

        Returns:
            ``BlockOption_Mt``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if setting is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, setting)

        self.value: typing.Final[tuple[any]] = types._Tuple([setting])
        self.setting: typing.Final[types.Integer] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``BlockOption_Mt`` from INP.

        Parameters:
            source: INP data card data option dawwg option option.

        Returns:
            ``BlockOption_Mt``.

        Raises:
            McnpError: SYNTAX_BLOCK_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = BlockOption_Mt._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_BLOCK_OPTION, source)

        setting = types.Integer.from_mcnp(tokens[1])

        return BlockOption_Mt(setting)
