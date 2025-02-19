import re
import typing

from . import _option
from .....utils import types
from .....utils import errors
from .....utils import _parser


class BlockOption_Nosigf(_option.BlockOption_, keyword='nosigf'):
    """
    Represents INP data card data option dawwg option nosigf options.

    Attributes:
        setting: Inhibit fission multiplication on/off.
    """

    _REGEX = re.compile(r'\Anosigf( \S+)\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``BlockOption_Nosigf``.

        Parameters:
            setting: Inhibit fission multiplication on/off.

        Returns:
            ``BlockOption_Nosigf``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if setting is None or setting.value not in {0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, setting)

        self.value: typing.Final[tuple[any]] = types._Tuple([setting])
        self.setting: typing.Final[types.Integer] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``BlockOption_Nosigf`` from INP.

        Parameters:
            source: INP data card data option dawwg option option.

        Returns:
            ``BlockOption_Nosigf``.

        Raises:
            InpError: SYNTAX_BLOCK_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = BlockOption_Nosigf._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        setting = types.Integer.from_mcnp(tokens[1])

        return BlockOption_Nosigf(setting)
