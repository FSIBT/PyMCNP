import re
import typing

from . import _option
from .....utils import types
from .....utils import errors
from .....utils import _parser


class BlockOption_Fluxone(_option.BlockOption_, keyword='fluxone'):
    """
    Represents INP data card data option dawwg option fluxone options.

    Attributes:
        setting: Flux override on/off.
    """

    _REGEX = re.compile(r'\Afluxone( \S+)\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``BlockOption_Fluxone``.

        Parameters:
            setting: Flux override on/off.

        Returns:
            ``BlockOption_Fluxone``.

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
        Generates ``BlockOption_Fluxone`` from INP.

        Parameters:
            source: INP data card data option dawwg option option.

        Returns:
            ``BlockOption_Fluxone``.

        Raises:
            McnpError: SYNTAX_BLOCK_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = BlockOption_Fluxone._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_BLOCK_OPTION, source)

        setting = types.Integer.from_mcnp(tokens[1])

        return BlockOption_Fluxone(setting)
