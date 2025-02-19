import re
import typing

from . import _option
from .....utils import types
from .....utils import errors
from .....utils import _parser


class BlockOption_Tsaepsi(_option.BlockOption_, keyword='tsaepsi'):
    """
    Represents INP data card data option dawwg option tsaepsi options.

    Attributes:
        setting: Convergence criteria for TSA sweeps.
    """

    _REGEX = re.compile(r'\Atsaepsi( \S+)\Z')

    def __init__(self, setting: types.Real):
        """
        Initializes ``BlockOption_Tsaepsi``.

        Parameters:
            setting: Convergence criteria for TSA sweeps.

        Returns:
            ``BlockOption_Tsaepsi``.

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
        Generates ``BlockOption_Tsaepsi`` from INP.

        Parameters:
            source: INP data card data option dawwg option option.

        Returns:
            ``BlockOption_Tsaepsi``.

        Raises:
            InpError: SYNTAX_BLOCK_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = BlockOption_Tsaepsi._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        setting = types.Real.from_mcnp(tokens[1])

        return BlockOption_Tsaepsi(setting)
