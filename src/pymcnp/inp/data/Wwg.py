import re
import typing
import dataclasses


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Wwg(DataOption_, keyword='wwg'):
    """
    Represents INP wwg elements.

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

    _ATTRS = {
        'tally': types.IntegerOrJump,
        'cell': types.IntegerOrJump,
        'lower': types.RealOrJump,
        'j1': types.Jump,
        'j2': types.Jump,
        'j3': types.Jump,
        'j4': types.Jump,
        'setting': types.IntegerOrJump,
    }

    _REGEX = re.compile(
        rf'\Awwg( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.Jump._REGEX.pattern})( {types.Jump._REGEX.pattern})( {types.Jump._REGEX.pattern})( {types.Jump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})\Z'
    )

    def __init__(
        self,
        tally: types.IntegerOrJump,
        cell: types.IntegerOrJump,
        lower: types.RealOrJump,
        j1: types.Jump,
        j2: types.Jump,
        j3: types.Jump,
        j4: types.Jump,
        setting: types.IntegerOrJump,
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

        self.tally: typing.Final[types.IntegerOrJump] = tally
        self.cell: typing.Final[types.IntegerOrJump] = cell
        self.lower: typing.Final[types.RealOrJump] = lower
        self.j1: typing.Final[types.Jump] = j1
        self.j2: typing.Final[types.Jump] = j2
        self.j3: typing.Final[types.Jump] = j3
        self.j4: typing.Final[types.Jump] = j4
        self.setting: typing.Final[types.IntegerOrJump] = setting


@dataclasses.dataclass
class WwgBuilder:
    """
    Builds ``Wwg``.

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

    tally: str | int | types.IntegerOrJump
    cell: str | int | types.IntegerOrJump
    lower: str | float | types.RealOrJump
    j1: str | types.Jump
    j2: str | types.Jump
    j3: str | types.Jump
    j4: str | types.Jump
    setting: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``WwgBuilder`` into ``Wwg``.

        Returns:
            ``Wwg`` for ``WwgBuilder``.
        """

        if isinstance(self.tally, types.Integer):
            tally = self.tally
        elif isinstance(self.tally, int):
            tally = types.IntegerOrJump(self.tally)
        elif isinstance(self.tally, str):
            tally = types.IntegerOrJump.from_mcnp(self.tally)

        if isinstance(self.cell, types.Integer):
            cell = self.cell
        elif isinstance(self.cell, int):
            cell = types.IntegerOrJump(self.cell)
        elif isinstance(self.cell, str):
            cell = types.IntegerOrJump.from_mcnp(self.cell)

        if isinstance(self.lower, types.Real):
            lower = self.lower
        elif isinstance(self.lower, float) or isinstance(self.lower, int):
            lower = types.RealOrJump(self.lower)
        elif isinstance(self.lower, str):
            lower = types.RealOrJump.from_mcnp(self.lower)

        if isinstance(self.j1, types.Jump):
            j1 = self.j1
        elif isinstance(self.j1, str):
            j1 = types.Jump.from_mcnp(self.j1)

        if isinstance(self.j2, types.Jump):
            j2 = self.j2
        elif isinstance(self.j2, str):
            j2 = types.Jump.from_mcnp(self.j2)

        if isinstance(self.j3, types.Jump):
            j3 = self.j3
        elif isinstance(self.j3, str):
            j3 = types.Jump.from_mcnp(self.j3)

        if isinstance(self.j4, types.Jump):
            j4 = self.j4
        elif isinstance(self.j4, str):
            j4 = types.Jump.from_mcnp(self.j4)

        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.IntegerOrJump(self.setting)
        elif isinstance(self.setting, str):
            setting = types.IntegerOrJump.from_mcnp(self.setting)

        return Wwg(
            tally=tally,
            cell=cell,
            lower=lower,
            j1=j1,
            j2=j2,
            j3=j3,
            j4=j4,
            setting=setting,
        )
