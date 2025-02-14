import re
import typing

from . import _option
from .....utils import types
from .....utils import errors
from .....utils import _parser


class BlockOption_Srcacc(_option.BlockOption_, keyword='srcacc'):
    """
    Represents INP data card data option dawwg option srcacc options.

    Attributes:
        setting: Transport accelerations.
    """

    _REGEX = re.compile(r'\Asrcacc( \S+)\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``BlockOption_Srcacc``.

        Parameters:
            setting: Transport accelerations.

        Returns:
            ``BlockOption_Srcacc``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if setting is None or setting not in {'dsa', 'tsa', 'no'}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, setting)

        self.value: typing.Final[tuple[any]] = types._Tuple([setting])
        self.setting: typing.Final[types.String] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``BlockOption_Srcacc`` from INP.

        Parameters:
            source: INP data card data option dawwg option option.

        Returns:
            ``BlockOption_Srcacc``.

        Raises:
            McnpError: SYNTAX_BLOCK_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = BlockOption_Srcacc._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_BLOCK_OPTION, source)

        setting = types.String.from_mcnp(tokens[1])

        return BlockOption_Srcacc(setting)
