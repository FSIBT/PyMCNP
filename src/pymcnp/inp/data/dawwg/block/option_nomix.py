import re
import typing

from . import _option
from .....utils import types
from .....utils import errors
from .....utils import _parser


class BlockOption_Nomix(_option.BlockOption_, keyword='nomix'):
    """
    Represents INP data card data option dawwg option nomix options.

    Attributes:
        setting: Suppress writing mixing on/off.
    """

    _REGEX = re.compile(r'\Anomix( \S+)\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``BlockOption_Nomix``.

        Parameters:
            setting: Suppress writing mixing on/off.

        Returns:
            ``BlockOption_Nomix``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if setting is None or setting.value not in {0, 1}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, setting)

        self.value: typing.Final[tuple[any]] = types._Tuple([setting])
        self.setting: typing.Final[types.Integer] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``BlockOption_Nomix`` from INP.

        Parameters:
            source: INP data card data option dawwg option option.

        Returns:
            ``BlockOption_Nomix``.

        Raises:
            McnpError: SYNTAX_BLOCK_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = BlockOption_Nomix._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_BLOCK_OPTION, source)

        setting = types.Integer.from_mcnp(tokens[1])

        return BlockOption_Nomix(setting)
