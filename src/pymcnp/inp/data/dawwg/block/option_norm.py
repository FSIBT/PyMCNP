import re
import typing

from . import _option
from .....utils import types
from .....utils import errors
from .....utils import _parser


class BlockOption_Norm(_option.BlockOption_, keyword='norm'):
    """
    Represents INP data card data option dawwg option norm options.

    Attributes:
        setting: Norm.
    """

    _REGEX = re.compile(r'\Anorm( \S+)\Z')

    def __init__(self, setting: types.Real):
        """
        Initializes ``BlockOption_Norm``.

        Parameters:
            setting: Norm.

        Returns:
            ``BlockOption_Norm``.

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
        Generates ``BlockOption_Norm`` from INP.

        Parameters:
            source: INP data card data option dawwg option option.

        Returns:
            ``BlockOption_Norm``.

        Raises:
            InpError: SYNTAX_BLOCK_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = BlockOption_Norm._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        setting = types.Real.from_mcnp(tokens[1])

        return BlockOption_Norm(setting)
