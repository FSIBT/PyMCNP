import re

from . import _option
from ... import types
from ... import errors


class Event(_option.PtracOption):
    """
    Represents INP `event` elements.
    """

    _KEYWORD = 'event'

    _ATTRS = {
        'settings': types.Tuple(types.String),
    }

    _REGEX = re.compile(rf'\Aevent((?: {types.String._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)

    def __init__(self, settings: list[str] | list[types.String]):
        """
        Initializes `Event`.

        Parameters:
            settings: Specifies the type of events written to the PTRAC file.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.settings: types.Tuple(types.String) = settings

    @property
    def settings(self) -> types.Tuple(types.String):
        """
        Specifies the type of events written to the PTRAC file

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._settings

    @settings.setter
    def settings(self, settings: list[str] | list[types.String]) -> None:
        """
        Sets `settings`.

        Parameters:
            settings: Specifies the type of events written to the PTRAC file.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if settings is not None:
            array = []
            for item in settings:
                if isinstance(item, types.String):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(types.String.from_mcnp(item))
            settings = types.Tuple(types.String)(array)

        if settings is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, settings)

        self._settings: types.Tuple(types.String) = settings
