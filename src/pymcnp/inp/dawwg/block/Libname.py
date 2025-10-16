import re

from . import _option
from .... import types
from .... import errors


class Libname(_option.BlockOption):
    """
    Represents INP `libname` elements.
    """

    _KEYWORD = 'libname'

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(rf'\Alibname( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, setting: str | types.String):
        """
        Initializes `Libname`.

        Parameters:
            setting: Cross-section file name.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.setting: types.String = setting

    @property
    def setting(self) -> types.String:
        """
        Cross-section file name

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._setting

    @setting.setter
    def setting(self, setting: str | types.String) -> None:
        """
        Sets `setting`.

        Parameters:
            setting: Cross-section file name.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if setting is not None:
            if isinstance(setting, types.String):
                setting = setting
            elif isinstance(setting, str):
                setting = types.String.from_mcnp(setting)

        if setting is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self._setting: types.String = setting
