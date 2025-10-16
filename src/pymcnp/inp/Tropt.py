import re

from . import tropt
from . import _card
from .. import types


class Tropt(_card.Card):
    """
    Represents INP `tropt` cards.
    """

    _KEYWORD = 'tropt'

    _ATTRS = {
        'options': types.Tuple(tropt.TroptOption),
    }

    _REGEX = re.compile(rf'\Atropt((?: (?:{tropt.TroptOption._REGEX.pattern[2:-2]}))+?)?\Z', re.IGNORECASE)

    def __init__(self, options: list[str] | list[tropt.TroptOption] = None):
        """
        Initializes `Tropt`.

        Parameters:
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.options: types.Tuple(tropt.TroptOption) = options

    @property
    def options(self) -> types.Tuple(tropt.TroptOption):
        """
        Dictionary of options

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._options

    @options.setter
    def options(self, options: list[str] | list[tropt.TroptOption]) -> None:
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
                if isinstance(item, tropt.TroptOption):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(tropt.TroptOption.from_mcnp(item))
            options = types.Tuple(tropt.TroptOption)(array)

        self._options: types.Tuple(tropt.TroptOption) = options
