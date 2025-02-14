import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class CellOption_Nonu(_option.CellOption_, keyword='nonu'):
    """
    Represents INP cell card nonu options.

    Attributes:
        setting: Cell fission setting.
    """

    _REGEX = re.compile(r'\Anonu( \S+)\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``CellOption_Nonu``.

        Parameters:
            setting: Cell fission setting.

        Returns:
            ``CellOption_Nonu``.

        Raises:
            McnpError: SEMANTICS_CELL_OPTION_VALUE.
        """

        if setting is None or setting.value not in {0, 1, 2}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_CELL_OPTION_VALUE, setting)

        self.value: typing.Final[tuple[any]] = types._Tuple([setting])
        self.setting: typing.Final[types.Integer] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``CellOption_Nonu`` from INP.

        Parameters:
            source: INP cell card option.

        Returns:
            ``CellOption_Nonu``.

        Raises:
            McnpError: SYNTAX_CELL_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = CellOption_Nonu._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_CELL_OPTION, source)

        setting = types.Integer.from_mcnp(tokens[1])

        return CellOption_Nonu(setting)
