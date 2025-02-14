import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Wwg(_option.DataOption_, keyword='wwg'):
    """
    Represents INP data card wwg options.

    Attributes:
        tally: Problem tally number.
        cell: Cell-based or mesh-based weight window generator.
        lower: Value of the generated lower weight-window bound for cell.
        j1: Placeholder jump #1.
        j2: Placeholder jump #2.
        j3: Placeholder jump #3.
        j4: Placeholder jump #4.
        setting: Energy- or time-dependent weight window toggle.
    """

    _REGEX = re.compile(r'\Awwg( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)\Z')

    def __init__(
        self,
        tally: types.Integer,
        cell: types.Integer,
        lower: types.Real,
        j1: types.Jump,
        j2: types.Jump,
        j3: types.Jump,
        j4: types.Jump,
        setting: types.Integer,
    ):
        """
        Initializes ``DataOption_Wwg``.

        Parameters:
            tally: Problem tally number.
            cell: Cell-based or mesh-based weight window generator.
            lower: Value of the generated lower weight-window bound for cell.
            j1: Placeholder jump #1.
            j2: Placeholder jump #2.
            j3: Placeholder jump #3.
            j4: Placeholder jump #4.
            setting: Energy- or time-dependent weight window toggle.

        Returns:
            ``DataOption_Wwg``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if tally is None or not (tally <= 99_999_999):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, tally)
        if cell is None or not (cell <= 99_999_999):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, cell)
        if lower is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, lower)
        if j1 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, j1)
        if j2 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, j2)
        if j3 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, j3)
        if j4 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, j4)
        if setting is None or setting.value not in {0, 1}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, setting)

        self.value: typing.Final[tuple[any]] = types._Tuple(
            [tally, cell, lower, j1, j2, j3, j4, setting]
        )
        self.tally: typing.Final[types.Integer] = tally
        self.cell: typing.Final[types.Integer] = cell
        self.lower: typing.Final[types.Real] = lower
        self.j1: typing.Final[types.Jump] = j1
        self.j2: typing.Final[types.Jump] = j2
        self.j3: typing.Final[types.Jump] = j3
        self.j4: typing.Final[types.Jump] = j4
        self.setting: typing.Final[types.Integer] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Wwg`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Wwg``.

        Raises:
            McnpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Wwg._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_DATA_OPTION, source)

        tally = types.Integer.from_mcnp(tokens[1])
        cell = types.Integer.from_mcnp(tokens[2])
        lower = types.Real.from_mcnp(tokens[3])
        j1 = types.Jump.from_mcnp(tokens[4])
        j2 = types.Jump.from_mcnp(tokens[5])
        j3 = types.Jump.from_mcnp(tokens[6])
        j4 = types.Jump.from_mcnp(tokens[7])
        setting = types.Integer.from_mcnp(tokens[8])

        return DataOption_Wwg(tally, cell, lower, j1, j2, j3, j4, setting)
