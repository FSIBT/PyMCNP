import re

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

    def __init__(self, tally: str | int | types.Integer, cell: str | int | types.Integer, lower: str | int | float | types.Real, setting: str | int | types.Integer = None):
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

        self.tally: types.Integer = tally
        self.cell: types.Integer = cell
        self.lower: types.Real = lower
        self.setting: types.Integer = setting

    @property
    def tally(self) -> types.Integer:
        """
        Gets ``tally``.

        Returns:
            ``tally``.
        """

        return self._tally

    @tally.setter
    def tally(self, tally: str | int | types.Integer) -> None:
        """
        Sets ``tally``.

        Parameters:
            tally: Problem tally number.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if tally is not None:
            if isinstance(tally, types.Integer):
                tally = tally
            elif isinstance(tally, int):
                tally = types.Integer(tally)
            elif isinstance(tally, str):
                tally = types.Integer.from_mcnp(tally)
            else:
                raise TypeError

        if tally is None or not (tally <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, tally)

        self._tally: types.Integer = tally

    @property
    def cell(self) -> types.Integer:
        """
        Gets ``cell``.

        Returns:
            ``cell``.
        """

        return self._cell

    @cell.setter
    def cell(self, cell: str | int | types.Integer) -> None:
        """
        Sets ``cell``.

        Parameters:
            cell: Cell-based or mesh-based weight window generator.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if cell is not None:
            if isinstance(cell, types.Integer):
                cell = cell
            elif isinstance(cell, int):
                cell = types.Integer(cell)
            elif isinstance(cell, str):
                cell = types.Integer.from_mcnp(cell)
            else:
                raise TypeError

        if cell is None or not (cell <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, cell)

        self._cell: types.Integer = cell

    @property
    def lower(self) -> types.Real:
        """
        Gets ``lower``.

        Returns:
            ``lower``.
        """

        return self._lower

    @lower.setter
    def lower(self, lower: str | int | float | types.Real) -> None:
        """
        Sets ``lower``.

        Parameters:
            lower: Value of the generated lower weight-window bound for cell.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if lower is not None:
            if isinstance(lower, types.Real):
                lower = lower
            elif isinstance(lower, int):
                lower = types.Real(lower)
            elif isinstance(lower, float):
                lower = types.Real(lower)
            elif isinstance(lower, str):
                lower = types.Real.from_mcnp(lower)
            else:
                raise TypeError

        if lower is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, lower)

        self._lower: types.Real = lower

    @property
    def setting(self) -> types.Integer:
        """
        Gets ``setting``.

        Returns:
            ``setting``.
        """

        return self._setting

    @setting.setter
    def setting(self, setting: str | int | types.Integer) -> None:
        """
        Sets ``setting``.

        Parameters:
            setting: Energy- or time-dependent weight window toggle.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if setting is not None:
            if isinstance(setting, types.Integer):
                setting = setting
            elif isinstance(setting, int):
                setting = types.Integer(setting)
            elif isinstance(setting, str):
                setting = types.Integer.from_mcnp(setting)
            else:
                raise TypeError

        self._setting: types.Integer = setting
