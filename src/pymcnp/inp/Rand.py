import re

from . import rand
from . import _card
from .. import types


class Rand(_card.Card):
    """
    Represents INP `rand` cards.
    """

    _KEYWORD = 'rand'

    _ATTRS = {
        'options': types.Tuple(rand.RandOption),
    }

    _REGEX = re.compile(rf'\Arand((?: (?:{rand.RandOption._REGEX.pattern[2:-2]}))+?)?\Z', re.IGNORECASE)

    def __init__(self, options: list[str] | list[rand.RandOption] = None):
        """
        Initializes `Rand`.

        Parameters:
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.options: types.Tuple(rand.RandOption) = options

    @property
    def options(self) -> types.Tuple(rand.RandOption):
        """
        Dictionary of options

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._options

    @options.setter
    def options(self, options: list[str] | list[rand.RandOption]) -> None:
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
                if isinstance(item, rand.RandOption):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(rand.RandOption.from_mcnp(item))
            options = types.Tuple(rand.RandOption)(array)

        self._options: types.Tuple(rand.RandOption) = options
