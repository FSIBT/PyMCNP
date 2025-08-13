import re

from . import _option
from ... import types
from ... import errors


class File(_option.PtracOption):
    """
    Represents INP `file` elements.
    """

    _KEYWORD = 'file'

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(r'\Afile(?: (asc|bin|aov|bov))\Z', re.IGNORECASE)

    def __init__(self, setting: str | types.String):
        """
        Initializes `File`.

        Parameters:
            setting: PTRAC file type.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.setting: types.String = setting

    @property
    def setting(self) -> types.String:
        """
        PTRAC file type

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
            setting: PTRAC file type.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if setting is not None:
            if isinstance(setting, types.String):
                setting = setting
            elif isinstance(setting, str):
                setting = types.String.from_mcnp(setting)

        if setting is None or setting.value.lower() not in {'asc', 'bin', 'aov', 'bov'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self._setting: types.String = setting
