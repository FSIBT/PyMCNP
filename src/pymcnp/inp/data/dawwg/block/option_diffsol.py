import re
import typing

from . import _option
from .....utils import types
from .....utils import errors
from .....utils import _parser


class BlockOption_Diffsol(_option.BlockOption_, keyword='diffsol'):
    """
    Represents INP data card data option dawwg option diffsol options.

    Attributes:
        setting: Diffusion operator solver.
    """

    _REGEX = re.compile(r'\Adiffsol( \S+)\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``BlockOption_Diffsol``.

        Parameters:
            setting: Diffusion operator solver.

        Returns:
            ``BlockOption_Diffsol``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if setting is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, setting)

        self.value: typing.Final[tuple[any]] = types._Tuple([setting])
        self.setting: typing.Final[types.String] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``BlockOption_Diffsol`` from INP.

        Parameters:
            source: INP data card data option dawwg option option.

        Returns:
            ``BlockOption_Diffsol``.

        Raises:
            InpError: SYNTAX_BLOCK_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = BlockOption_Diffsol._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        setting = types.String.from_mcnp(tokens[1])

        return BlockOption_Diffsol(setting)
