import re

from . import ssr
from . import _card
from .. import types


class Ssr(_card.Card):
    """
    Represents INP `ssr` cards.
    """

    _KEYWORD = 'ssr'

    _ATTRS = {
        'options': types.Tuple(ssr.SsrOption),
    }

    _REGEX = re.compile(rf'\Assr((?: (?:{ssr.SsrOption._REGEX.pattern[2:-2]}))+?)?\Z', re.IGNORECASE)

    def __init__(self, options: list[str] | list[ssr.SsrOption] = None):
        """
        Initializes `Ssr`.

        Parameters:
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.options: types.Tuple(ssr.SsrOption) = options

    @property
    def options(self) -> types.Tuple(ssr.SsrOption):
        """
        Dictionary of options

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._options

    @options.setter
    def options(self, options: list[str] | list[ssr.SsrOption]) -> None:
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
                if isinstance(item, ssr.SsrOption):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(ssr.SsrOption.from_mcnp(item))
            options = types.Tuple(ssr.SsrOption)(array)

        self._options: types.Tuple(ssr.SsrOption) = options
