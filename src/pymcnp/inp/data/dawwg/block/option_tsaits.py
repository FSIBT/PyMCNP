import re
import typing

from . import _option
from .....utils import types
from .....utils import errors
from .....utils import _parser


class BlockOption_Tsaits(_option.BlockOption_, keyword='tsaits'):
    """
    Represents INP data card data option dawwg option tsaits options.

    Attributes:
        setting: Maximum TSA iteration count.
    """

    _REGEX = re.compile(r'\Atsaits( \S+)\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``BlockOption_Tsaits``.

        Parameters:
            setting: Maximum TSA iteration count.

        Returns:
            ``BlockOption_Tsaits``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if setting is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, setting)

        self.value: typing.Final[tuple[any]] = types._Tuple([setting])
        self.setting: typing.Final[types.Integer] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``BlockOption_Tsaits`` from INP.

        Parameters:
            source: INP data card data option dawwg option option.

        Returns:
            ``BlockOption_Tsaits``.

        Raises:
            InpError: SYNTAX_BLOCK_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = BlockOption_Tsaits._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        setting = types.Integer.from_mcnp(tokens[1])

        return BlockOption_Tsaits(setting)
