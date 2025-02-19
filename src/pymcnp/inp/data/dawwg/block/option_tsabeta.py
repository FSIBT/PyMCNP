import re
import typing

from . import _option
from .....utils import types
from .....utils import errors
from .....utils import _parser


class BlockOption_Tsabeta(_option.BlockOption_, keyword='tsabeta'):
    """
    Represents INP data card data option dawwg option tsabeta options.

    Attributes:
        setting: Scattering cross-section reduction for TSA.
    """

    _REGEX = re.compile(r'\Atsabeta( \S+)\Z')

    def __init__(self, setting: types.Real):
        """
        Initializes ``BlockOption_Tsabeta``.

        Parameters:
            setting: Scattering cross-section reduction for TSA.

        Returns:
            ``BlockOption_Tsabeta``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if setting is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, setting)

        self.value: typing.Final[tuple[any]] = types._Tuple([setting])
        self.setting: typing.Final[types.Real] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``BlockOption_Tsabeta`` from INP.

        Parameters:
            source: INP data card data option dawwg option option.

        Returns:
            ``BlockOption_Tsabeta``.

        Raises:
            InpError: SYNTAX_BLOCK_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = BlockOption_Tsabeta._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        setting = types.Real.from_mcnp(tokens[1])

        return BlockOption_Tsabeta(setting)
