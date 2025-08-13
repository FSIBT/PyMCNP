import re

from . import _option
from ... import types
from ... import errors


class Col(_option.SsrOption):
    """
    Represents INP `col` elements.
    """

    _KEYWORD = 'col'

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Acol( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, setting: str | int | types.Integer):
        """
        Initializes `Col`.

        Parameters:
            setting: Collision option setting.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.setting: types.Integer = setting

    @property
    def setting(self) -> types.Integer:
        """
        Collision option setting

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
            setting: Collision option setting.

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

        if setting is None or setting not in {-1, 0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self._setting: types.Integer = setting
