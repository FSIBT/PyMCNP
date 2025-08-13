import re

from . import _card
from .. import types


class Nonu(_card.Card):
    """
    Represents INP `nonu` cards.
    """

    _KEYWORD = 'nonu'

    _ATTRS = {
        'settings': types.Tuple(types.Integer),
    }

    _REGEX = re.compile(rf'\Anonu((?: {types.Integer._REGEX.pattern[2:-2]})+?)?\Z', re.IGNORECASE)

    def __init__(self, settings: list[str] | list[int] | list[types.Integer] = None):
        """
        Initializes `Nonu`.

        Parameters:
            settings: Tuple of fission settings.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.settings: types.Tuple(types.Integer) = settings

    @property
    def settings(self) -> types.Tuple(types.Integer):
        """
        Tuple of fission settings

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._settings

    @settings.setter
    def settings(self, settings: list[str] | list[int] | list[types.Integer]) -> None:
        """
        Sets `settings`.

        Parameters:
            settings: Tuple of fission settings.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if settings is not None:
            array = []
            for item in settings:
                if isinstance(item, types.Integer):
                    array.append(item)
                elif isinstance(item, int):
                    array.append(types.Integer(item))
                elif isinstance(item, str):
                    array.append(types.Integer.from_mcnp(item))
            settings = types.Tuple(types.Integer)(array)

        self._settings: types.Tuple(types.Integer) = settings
