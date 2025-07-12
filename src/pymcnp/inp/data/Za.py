import re

from . import _option
from ...utils import types


class Za(_option.DataOption):
    """
    Represents INP za elements.
    """

    _KEYWORD = 'za'

    _ATTRS = {
        'anything': types.String,
    }

    _REGEX = re.compile(rf'\Aza( {types.String._REGEX.pattern[2:-2]})?\Z')

    def __init__(self, anything: str | types.String = None):
        """
        Initializes ``Za``.

        Parameters:
            anything: Any parameters.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.anything: types.String = anything

    @property
    def anything(self) -> types.String:
        """
        Any parameters

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._anything

    @anything.setter
    def anything(self, anything: str | types.String) -> None:
        """
        Sets ``anything``.

        Parameters:
            anything: Any parameters.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if anything is not None:
            if isinstance(anything, types.String):
                anything = anything
            elif isinstance(anything, str):
                anything = types.String.from_mcnp(anything)

        self._anything: types.String = anything
