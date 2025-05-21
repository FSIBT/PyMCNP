import re
import copy
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Wwg(DataOption):
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

    _KEYWORD = 'wwg'

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
        rf'\Awwg( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Jump._REGEX.pattern})( {types.Jump._REGEX.pattern})( {types.Jump._REGEX.pattern})( {types.Jump._REGEX.pattern})( {types.Integer._REGEX.pattern})\Z'
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
            InpError: SEMANTICS_OPTION.
        """

        if tally is None or not (tally.value <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, tally)
        if cell is None or not (cell.value <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, cell)
        if lower is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, lower)
        if j1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, j1)
        if j2 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, j2)
        if j3 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, j3)
        if j4 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, j4)
        if setting is None or setting.value not in {0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

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

    tally: str | int | types.Integer
    cell: str | int | types.Integer
    lower: str | float | types.Real
    j1: str | types.Jump
    j2: str | types.Jump
    j3: str | types.Jump
    j4: str | types.Jump
    setting: str | int | types.Integer

    def build(self):
        """
        Builds ``WwgBuilder`` into ``Wwg``.

        Returns:
            ``Wwg`` for ``WwgBuilder``.
        """

        tally = self.tally
        if isinstance(self.tally, types.Integer):
            tally = self.tally
        elif isinstance(self.tally, int):
            tally = types.Integer(self.tally)
        elif isinstance(self.tally, str):
            tally = types.Integer.from_mcnp(self.tally)

        cell = self.cell
        if isinstance(self.cell, types.Integer):
            cell = self.cell
        elif isinstance(self.cell, int):
            cell = types.Integer(self.cell)
        elif isinstance(self.cell, str):
            cell = types.Integer.from_mcnp(self.cell)

        lower = self.lower
        if isinstance(self.lower, types.Real):
            lower = self.lower
        elif isinstance(self.lower, float) or isinstance(self.lower, int):
            lower = types.Real(self.lower)
        elif isinstance(self.lower, str):
            lower = types.Real.from_mcnp(self.lower)

        j1 = self.j1
        if isinstance(self.j1, types.Jump):
            j1 = self.j1
        elif isinstance(self.j1, str):
            j1 = types.Jump.from_mcnp(self.j1)

        j2 = self.j2
        if isinstance(self.j2, types.Jump):
            j2 = self.j2
        elif isinstance(self.j2, str):
            j2 = types.Jump.from_mcnp(self.j2)

        j3 = self.j3
        if isinstance(self.j3, types.Jump):
            j3 = self.j3
        elif isinstance(self.j3, str):
            j3 = types.Jump.from_mcnp(self.j3)

        j4 = self.j4
        if isinstance(self.j4, types.Jump):
            j4 = self.j4
        elif isinstance(self.j4, str):
            j4 = types.Jump.from_mcnp(self.j4)

        setting = self.setting
        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.Integer(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Integer.from_mcnp(self.setting)

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

    @staticmethod
    def unbuild(ast: Wwg):
        """
        Unbuilds ``Wwg`` into ``WwgBuilder``

        Returns:
            ``WwgBuilder`` for ``Wwg``.
        """

        return Wwg(
            tally=copy.deepcopy(ast.tally),
            cell=copy.deepcopy(ast.cell),
            lower=copy.deepcopy(ast.lower),
            j1=copy.deepcopy(ast.j1),
            j2=copy.deepcopy(ast.j2),
            j3=copy.deepcopy(ast.j3),
            j4=copy.deepcopy(ast.j4),
            setting=copy.deepcopy(ast.setting),
        )
