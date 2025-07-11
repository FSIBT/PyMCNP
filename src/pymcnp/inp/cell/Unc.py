import re

from . import _option
from ...utils import types
from ...utils import errors


class Unc(_option.CellOption):
    """
    Represents INP unc elements.

    Attributes:
        designator: Cell particle designator.
        setting: Cell uncollided secondaries setting.
    """

    _KEYWORD = 'unc'

    _ATTRS = {
        'designator': types.Designator,
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Aunc:(\S+)( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, designator: str | types.Designator, setting: str | int | types.Integer):
        """
        Initializes ``Unc``.

        Parameters:
            designator: Cell particle designator.
            setting: Cell uncollided secondaries setting.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.designator: types.Designator = designator
        self.setting: types.Integer = setting

    @property
    def designator(self) -> types.Designator:
        """
        Gets ``designator``.

        Returns:
            ``designator``.
        """

        return self._designator

    @designator.setter
    def designator(self, designator: str | types.Designator) -> None:
        """
        Sets ``designator``.

        Parameters:
            designator: Cell particle designator.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if designator is not None:
            if isinstance(designator, types.Designator):
                designator = designator
            elif isinstance(designator, str):
                designator = types.Designator.from_mcnp(designator)
            else:
                raise TypeError

        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, designator)

        self._designator: types.Designator = designator

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
            setting: Cell uncollided secondaries setting.

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

        if setting is None or setting not in {0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self._setting: types.Integer = setting
