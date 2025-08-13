import re

from . import kopts
from . import _card
from .. import types


class Kopts(_card.Card):
    """
    Represents INP `kopts` cards.
    """

    _KEYWORD = 'kopts'

    _ATTRS = {
        'options': types.Tuple(kopts.KoptsOption),
    }

    _REGEX = re.compile(rf'\Akopts((?: (?:{kopts.KoptsOption._REGEX.pattern[2:-2]}))+?)?\Z', re.IGNORECASE)

    def __init__(self, options: list[str] | list[kopts.KoptsOption] = None):
        """
        Initializes `Kopts`.

        Parameters:
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.options: types.Tuple(kopts.KoptsOption) = options

    @property
    def options(self) -> types.Tuple(kopts.KoptsOption):
        """
        Dictionary of options

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._options

    @options.setter
    def options(self, options: list[str] | list[kopts.KoptsOption]) -> None:
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
                if isinstance(item, kopts.KoptsOption):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(kopts.KoptsOption.from_mcnp(item))
            options = types.Tuple(kopts.KoptsOption)(array)

        self._options: types.Tuple(kopts.KoptsOption) = options
