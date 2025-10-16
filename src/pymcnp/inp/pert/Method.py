import re

from . import _option
from ... import types
from ... import errors


class Method(_option.PertOption):
    """
    Represents INP `method` elements.
    """

    _KEYWORD = 'method'

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Amethod( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, setting: str | int | types.Integer):
        """
        Initializes `Method`.

        Parameters:
            setting: Printing and specifies setting.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.setting: types.Integer = setting

    @property
    def setting(self) -> types.Integer:
        """
        Printing and specifies setting

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._setting

    @setting.setter
    def setting(self, setting: str | int | types.Integer) -> None:
        """
        Sets `setting`.

        Parameters:
            setting: Printing and specifies setting.

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

        if setting is None or setting not in {1, -1, 2, -2, 3, -3}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self._setting: types.Integer = setting
