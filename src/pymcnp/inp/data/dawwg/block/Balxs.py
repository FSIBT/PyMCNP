import re

from . import _option
from .....utils import types
from .....utils import errors


class Balxs(_option.BlockOption):
    """
    Represents INP balxs elements.

    Attributes:
        setting: Cross-section balance control.
    """

    _KEYWORD = 'balxs'

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Abalxs( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: str | int | types.Integer):
        """
        Initializes ``Balxs``.

        Parameters:
            setting: Cross-section balance control.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.setting: types.Integer = setting

    @property
    def setting(self) -> types.Integer:
        """
        Gets ``setting``.

        Returns:
            ``setting``.
        """

        return self._setting

    @setting.setter
    def setting(self, setting: str | int | types.Integer) -> None:
        """
        Sets ``setting``.

        Parameters:
            setting: Cross-section balance control.

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
            else:
                raise TypeError

        if setting is None or setting not in {-1, 0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self._setting: types.Integer = setting
