import re
import typing

from . import _option
from .....utils import types
from .....utils import errors
from .....utils import _parser


class BlockOption_Noslnp(_option.BlockOption_, keyword='noslnp'):
    """
    Represents INP data card data option dawwg option noslnp options.

    Attributes:
        setting: Suppress writing SOLINP on/off.
    """

    _REGEX = re.compile(r'\Anoslnp( \S+)\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``BlockOption_Noslnp``.

        Parameters:
            setting: Suppress writing SOLINP on/off.

        Returns:
            ``BlockOption_Noslnp``.

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
        Generates ``BlockOption_Noslnp`` from INP.

        Parameters:
            source: INP data card data option dawwg option option.

        Returns:
            ``BlockOption_Noslnp``.

        Raises:
            McnpError: SYNTAX_BLOCK_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = BlockOption_Noslnp._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_BLOCK_OPTION, source)

        setting = types.Integer.from_mcnp(tokens[1])

        return BlockOption_Noslnp(setting)
