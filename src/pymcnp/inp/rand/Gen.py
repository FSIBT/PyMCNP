import re

from . import _option
from ... import types
from ... import errors


class Gen(_option.RandOption):
    """
    Represents INP `gen` elements.
    """

    _KEYWORD = 'gen'

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Agen( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, setting: str | int | types.Integer):
        """
        Initializes `Gen`.

        Parameters:
            setting: Type of pseudorandom number generator.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.setting: types.Integer = setting

    @property
    def setting(self) -> types.Integer:
        """
        Type of pseudorandom number generator

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
            setting: Type of pseudorandom number generator.

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

        if setting is None or setting not in {1, 2, 3, 4}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self._setting: types.Integer = setting
