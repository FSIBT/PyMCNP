import re

from . import _option
from ... import types
from ... import errors


class Nonu(_option.LikeOption):
    """
    Represents INP `nonu` elements.
    """

    _KEYWORD = 'nonu'

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Anonu( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, setting: str | int | types.Integer):
        """
        Initializes `Nonu`.

        Parameters:
            setting: Cell fission setting.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.setting: types.Integer = setting

    @property
    def setting(self) -> types.Integer:
        """
        Gets `setting`.

        Returns:
            `setting`.
        """

        return self._setting

    @setting.setter
    def setting(self, setting: str | int | types.Integer) -> None:
        """
        Sets `setting`.

        Parameters:
            setting: Cell fission setting.

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

        if setting is None or setting not in {0, 1, 2}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self._setting: types.Integer = setting
