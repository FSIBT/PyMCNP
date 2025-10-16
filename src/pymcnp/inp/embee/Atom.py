import re

from . import _option
from ... import types
from ... import errors


class Atom(_option.EmbeeOption):
    """
    Represents INP `atom` elements.
    """

    _KEYWORD = 'atom'

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(rf'\Aatom( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, setting: str | types.String):
        """
        Initializes `Atom`.

        Parameters:
            setting: Flag to multiply by atom density.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.setting: types.String = setting

    @property
    def setting(self) -> types.String:
        """
        Flag to multiply by atom density

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
            setting: Flag to multiply by atom density.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if setting is not None:
            if isinstance(setting, types.String):
                setting = setting
            elif isinstance(setting, str):
                setting = types.String.from_mcnp(setting)

        if setting is None or setting.value.lower() not in {'yes', 'no'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self._setting: types.String = setting
