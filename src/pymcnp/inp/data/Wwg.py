import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Wwg(_option.DataOption):
    """
    Represents INP wwg elements.

    Attributes:
        tally: Problem tally number.
        cell: Cell-based or mesh-based weight window generator.
        lower: Value of the generated lower weight-window bound for cell.
        setting: Energy- or time-dependent weight window toggle.
    """

    _KEYWORD = 'wwg'

    _ATTRS = {
        'tally': types.Integer,
        'cell': types.Integer,
        'lower': types.Real,
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Awwg( {types.Integer._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})?\Z')

    def __init__(self, tally: types.Integer, cell: types.Integer, lower: types.Real, setting: types.Integer = None):
        """
        Initializes ``Wwg``.

        Parameters:
            tally: Problem tally number.
            cell: Cell-based or mesh-based weight window generator.
            lower: Value of the generated lower weight-window bound for cell.
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

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                tally,
                cell,
                lower,
                setting,
            ]
        )

        self.tally: typing.Final[types.Integer] = tally
        self.cell: typing.Final[types.Integer] = cell
        self.lower: typing.Final[types.Real] = lower
        self.setting: typing.Final[types.Integer] = setting


@dataclasses.dataclass
class WwgBuilder(_option.DataOptionBuilder):
    """
    Builds ``Wwg``.

    Attributes:
        tally: Problem tally number.
        cell: Cell-based or mesh-based weight window generator.
        lower: Value of the generated lower weight-window bound for cell.
        setting: Energy- or time-dependent weight window toggle.
    """

    tally: str | int | types.Integer
    cell: str | int | types.Integer
    lower: str | float | types.Real
    setting: str | int | types.Integer = None

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
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Wwg):
        """
        Unbuilds ``Wwg`` into ``WwgBuilder``

        Returns:
            ``WwgBuilder`` for ``Wwg``.
        """

        return WwgBuilder(
            tally=copy.deepcopy(ast.tally),
            cell=copy.deepcopy(ast.cell),
            lower=copy.deepcopy(ast.lower),
            setting=copy.deepcopy(ast.setting),
        )
