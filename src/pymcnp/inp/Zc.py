import re

from . import _card
from .. import types


class Zc(_card.Card):
    """
    Represents INP `zc` cards.
    """

    _KEYWORD = 'zc'

    _ATTRS = {
        'anything': types.String,
    }

    _REGEX = re.compile(rf'\Azc( {types.String._REGEX.pattern[2:-2]})?\Z', re.IGNORECASE)

    def __init__(self, anything: str | types.String = None):
        """
        Initializes `Zc`.

        Parameters:
            anything: Any parameters.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.anything: types.String = anything

    @property
    def anything(self) -> types.String:
        """
        Any parameters

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._anything

    @anything.setter
    def anything(self, anything: str | types.String) -> None:
        """
        Sets `anything`.

        Parameters:
            anything: Any parameters.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if anything is not None:
            if isinstance(anything, types.String):
                anything = anything
            elif isinstance(anything, str):
                anything = types.String.from_mcnp(anything)

        self._anything: types.String = anything
