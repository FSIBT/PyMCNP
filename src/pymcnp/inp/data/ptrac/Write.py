import re

from . import _option
from ....utils import types
from ....utils import errors


class Write(_option.PtracOption):
    """
    Represents INP write elements.

    Attributes:
        setting: Controls what particle parameters are written.
    """

    _KEYWORD = 'write'

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(r'\Awrite(?: (pos|all))\Z')

    def __init__(self, setting: str | types.String):
        """
        Initializes ``Write``.

        Parameters:
            setting: Controls what particle parameters are written.

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
            else:
                raise TypeError

        if setting is None or setting not in {'pos', 'all'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self._setting: types.String = setting
