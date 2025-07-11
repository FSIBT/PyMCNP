import re

from . import _option
from ....utils import types
from ....utils import errors


class Conic(_option.PtracOption):
    """
    Represents INP conic elements.

    Attributes:
        setting: Activates a PTRAC file format specifically for coincidence tally scoring.
    """

    _KEYWORD = 'conic'

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(r'\Aconic(?: (col|lin))\Z')

    def __init__(self, setting: str | types.String):
        """
        Initializes ``Conic``.

        Parameters:
            setting: Activates a PTRAC file format specifically for coincidence tally scoring.

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
            setting: Activates a PTRAC file format specifically for coincidence tally scoring.

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

        if setting is None or setting not in {'col', 'lin'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self._setting: types.String = setting
