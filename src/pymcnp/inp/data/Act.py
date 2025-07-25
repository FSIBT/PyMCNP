import re

from . import act
from . import _option
from ... import types


class Act(_option.DataOption):
    """
    Represents INP act elements.
    """

    _KEYWORD = 'act'

    _ATTRS = {
        'options': types.Tuple(act.ActOption),
    }

    _REGEX = re.compile(rf'\Aact((?: (?:{act.ActOption._REGEX.pattern[2:-2]}))+?)?\Z', re.IGNORECASE)

    def __init__(self, options: list[str] | list[act.ActOption] = None):
        """
        Initializes ``Act``.

        Parameters:
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.options: types.Tuple(act.ActOption) = options

    @property
    def options(self) -> types.Tuple(act.ActOption):
        """
        Dictionary of options

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._options

    @options.setter
    def options(self, options: list[str] | list[act.ActOption]) -> None:
        """
        Sets ``options``.

        Parameters:
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if options is not None:
            array = []
            for item in options:
                if isinstance(item, act.ActOption):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(act.ActOption.from_mcnp(item))
            options = types.Tuple(act.ActOption)(array)

        self._options: types.Tuple(act.ActOption) = options
