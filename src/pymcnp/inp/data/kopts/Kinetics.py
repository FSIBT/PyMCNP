import re

from . import _option
from ....utils import types
from ....utils import errors


class Kinetics(_option.KoptsOption):
    """
    Represents INP kinetics elements.

    Attributes:
        setting: Yes/No calculate point-kinetics parameters.
    """

    _KEYWORD = 'kinetics'

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(rf'\Akinetics( {types.String._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: str | types.String):
        """
        Initializes ``Kinetics``.

        Parameters:
            setting: Yes/No calculate point-kinetics parameters.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.setting: types.String = setting

    @property
    def setting(self) -> types.String:
        """
        Gets ``setting``.

        Returns:
            ``setting``.
        """

        return self._setting

    @setting.setter
    def setting(self, setting: str | types.String) -> None:
        """
        Sets ``setting``.

        Parameters:
            setting: Yes/No calculate point-kinetics parameters.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if setting is not None:
            if isinstance(setting, types.String):
                setting = setting
            elif isinstance(setting, str):
                setting = types.String.from_mcnp(setting)
            else:
                raise TypeError

        if setting is None or setting not in {'yes', 'no'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self._setting: types.String = setting
