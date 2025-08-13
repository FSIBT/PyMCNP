import re

from . import _option
from .... import types
from .... import errors


class Byvolp(_option.BlockOption):
    """
    Represents INP `byvolp` elements.
    """

    _KEYWORD = 'byvolp'

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Abyvolp( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, setting: str | int | types.Integer):
        """
        Initializes `Byvolp`.

        Parameters:
            setting: Printed point reactions rates on/off.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.setting: types.Integer = setting

    @property
    def setting(self) -> types.Integer:
        """
        Printed point reactions rates on/off

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
            setting: Printed point reactions rates on/off.

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

        if setting is None or setting not in {0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self._setting: types.Integer = setting
