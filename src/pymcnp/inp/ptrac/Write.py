import re

from . import _option
from ... import types
from ... import errors


class Write(_option.PtracOption):
    """
    Represents INP `write` elements.
    """

    _KEYWORD = 'write'

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(r'\Awrite(?: (pos|all))\Z', re.IGNORECASE)

    def __init__(self, setting: str | types.String):
        """
        Initializes `Write`.

        Parameters:
            setting: Controls what particle parameters are written.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.setting: types.String = setting

    @property
    def setting(self) -> types.String:
        """
        Controls what particle parameters are written

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
            setting: Controls what particle parameters are written.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if setting is not None:
            if isinstance(setting, types.String):
                setting = setting
            elif isinstance(setting, str):
                setting = types.String.from_mcnp(setting)

        if setting is None or setting.value.lower() not in {'pos', 'all'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self._setting: types.String = setting
