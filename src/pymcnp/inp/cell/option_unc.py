import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class CellOption_Unc(_option.CellOption_, keyword='unc'):
    """
    Represents INP cell card unc options.

    Attributes:
        setting: Cell uncollided secondaries setting.
        designator: Cell particle designator.
    """

    _REGEX = re.compile(r'\Aunc:(\S+?)( \S+)\Z')

    def __init__(self, setting: types.Integer, designator: types.Designator):
        """
        Initializes ``CellOption_Unc``.

        Parameters:
            setting: Cell uncollided secondaries setting.
            designator: Cell particle designator.

        Returns:
            ``CellOption_Unc``.

        Raises:
            McnpError: SEMANTICS_CELL_OPTION_VALUE.
            McnpError: SEMANTICS_CELL_OPTION_DESIGNATOR.
        """

        if setting is None or setting.value not in {0, 1}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_CELL_OPTION_VALUE, setting)
        if designator is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_CELL_OPTION_DESIGNATOR, designator)

        self.value: typing.Final[tuple[any]] = types._Tuple([setting])
        self.setting: typing.Final[types.Integer] = setting
        self.designator: typing.Final[types.Designator] = designator

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``CellOption_Unc`` from INP.

        Parameters:
            source: INP cell card option.

        Returns:
            ``CellOption_Unc``.

        Raises:
            McnpError: SYNTAX_CELL_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = CellOption_Unc._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_CELL_OPTION, source)

        designator = types.Designator.from_mcnp(tokens[1])
        setting = types.Integer.from_mcnp(tokens[2])

        return CellOption_Unc(setting, designator)
