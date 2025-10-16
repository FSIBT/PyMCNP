import re

from . import _option
from .... import types
from .... import errors


class Srcacc(_option.BlockOption):
    """
    Represents INP `srcacc` elements.
    """

    _KEYWORD = 'srcacc'

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(rf'\Asrcacc( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, setting: str | types.String):
        """
        Initializes `Srcacc`.

        Parameters:
            setting: Transport accelerations.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.setting: types.String = setting

    @property
    def setting(self) -> types.String:
        """
        Transport accelerations

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
            setting: Transport accelerations.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if setting is not None:
            if isinstance(setting, types.String):
                setting = setting
            elif isinstance(setting, str):
                setting = types.String.from_mcnp(setting)

        if setting is None or setting.value.lower() not in {'dsa', 'tsa', 'no'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self._setting: types.String = setting
