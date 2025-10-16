import re

from . import stop
from . import _card
from .. import types


class Stop(_card.Card):
    """
    Represents INP `stop` cards.
    """

    _KEYWORD = 'stop'

    _ATTRS = {
        'options': types.Tuple(stop.StopOption),
    }

    _REGEX = re.compile(rf'\Astop((?: (?:{stop.StopOption._REGEX.pattern[2:-2]}))+?)?\Z', re.IGNORECASE)

    def __init__(self, options: list[str] | list[stop.StopOption] = None):
        """
        Initializes `Stop`.

        Parameters:
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.options: types.Tuple(stop.StopOption) = options

    @property
    def options(self) -> types.Tuple(stop.StopOption):
        """
        Dictionary of options

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._options

    @options.setter
    def options(self, options: list[str] | list[stop.StopOption]) -> None:
        """
        Sets `options`.

        Parameters:
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if options is not None:
            array = []
            for item in options:
                if isinstance(item, stop.StopOption):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(stop.StopOption.from_mcnp(item))
            options = types.Tuple(stop.StopOption)(array)

        self._options: types.Tuple(stop.StopOption) = options
