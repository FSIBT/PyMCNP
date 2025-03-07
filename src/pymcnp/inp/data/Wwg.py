import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Wwg(DataOption_, keyword='wwg'):
    """
    Represents INP wwg elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'tally': types.Integer,
        'cell': types.Integer,
        'lower': types.Real,
        'j1': types.Jump,
        'j2': types.Jump,
        'j3': types.Jump,
        'j4': types.Jump,
        'setting': types.Integer,
    }

    _REGEX = re.compile(
        rf'wwg( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Jump._REGEX.pattern})( {types.Jump._REGEX.pattern})( {types.Jump._REGEX.pattern})( {types.Jump._REGEX.pattern})( {types.Integer._REGEX.pattern})'
    )

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
        Initializes ``Wwg``.

        Parameters:
            tally: Problem tally number.
            cell: Cell-based or mesh-based weight window generator.
            lower: Value of the generated lower weight-window bound for cell.
            j1: Placeholder jump #1.
            j2: Placeholder jump #2.
            j3: Placeholder jump #3.
            j4: Placeholder jump #4.
            setting: Energy- or time-dependent weight window toggle.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if tally is None or not (tally <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, tally)
        if cell is None or not (cell <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, cell)
        if lower is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, lower)
        if j1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, j1)
        if j2 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, j2)
        if j3 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, j3)
        if j4 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, j4)
        if setting is None or setting.value not in {0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                tally,
                cell,
                lower,
                j1,
                j2,
                j3,
                j4,
                setting,
            ]
        )

        self.tally: typing.Final[types.Integer] = tally
        self.cell: typing.Final[types.Integer] = cell
        self.lower: typing.Final[types.Real] = lower
        self.j1: typing.Final[types.Jump] = j1
        self.j2: typing.Final[types.Jump] = j2
        self.j3: typing.Final[types.Jump] = j3
        self.j4: typing.Final[types.Jump] = j4
        self.setting: typing.Final[types.Integer] = setting
