import re

from . import mplot
from . import _card
from .. import types


class Mplot(_card.Card):
    """
    Represents INP `mplot` cards.
    """

    _KEYWORD = 'mplot'

    _ATTRS = {
        'options': types.Tuple(mplot.MplotOption),
    }

    _REGEX = re.compile(rf'\Amplot((?: (?:{mplot.MplotOption._REGEX.pattern[2:-2]}))+?)?\Z', re.IGNORECASE)

    def __init__(self, options: list[str] | list[mplot.MplotOption] = None):
        """
        Initializes `Mplot`.

        Parameters:
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.options: types.Tuple(mplot.MplotOption) = options

    @property
    def options(self) -> types.Tuple(mplot.MplotOption):
        """
        Dictionary of options

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._options

    @options.setter
    def options(self, options: list[str] | list[mplot.MplotOption]) -> None:
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
                if isinstance(item, mplot.MplotOption):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(mplot.MplotOption.from_mcnp(item))
            options = types.Tuple(mplot.MplotOption)(array)

        self._options: types.Tuple(mplot.MplotOption) = options
