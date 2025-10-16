import re

from . import _card
from .. import types
from .. import errors


class Mphys(_card.Card):
    """
    Represents INP `mphys` cards.
    """

    _KEYWORD = 'mphys'

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(rf'\Amphys( {types.String._REGEX.pattern[2:-2]})?\Z', re.IGNORECASE)

    def __init__(self, setting: str | types.String = None):
        """
        Initializes `Mphys`.

        Parameters:
            setting: Physics models on/off.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.setting: types.String = setting

    @property
    def setting(self) -> types.String:
        """
        Physics models on/off

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._setting

    @setting.setter
    def setting(self, setting: str | types.String) -> None:
        """
        Sets `setting`.

        Parameters:
            setting: Physics models on/off.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if setting is not None:
            if isinstance(setting, types.String):
                setting = setting
            elif isinstance(setting, str):
                setting = types.String.from_mcnp(setting)

        if setting is not None and setting.value.lower() not in {'on', 'off'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, setting)

        self._setting: types.String = setting
