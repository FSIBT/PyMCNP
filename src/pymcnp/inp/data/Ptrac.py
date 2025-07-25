import re

from . import ptrac
from . import _option
from ... import types


class Ptrac(_option.DataOption):
    """
    Represents INP ptrac elements.
    """

    _KEYWORD = 'ptrac'

    _ATTRS = {
        'options': types.Tuple(ptrac.PtracOption),
    }

    _REGEX = re.compile(rf'\Aptrac((?: (?:{ptrac.PtracOption._REGEX.pattern[2:-2]}))+?)?\Z', re.IGNORECASE)

    def __init__(self, options: list[str] | list[ptrac.PtracOption] = None):
        """
        Initializes ``Ptrac``.

        Parameters:
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.options: types.Tuple(ptrac.PtracOption) = options

    @property
    def options(self) -> types.Tuple(ptrac.PtracOption):
        """
        Dictionary of options

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._options

    @options.setter
    def options(self, options: list[str] | list[ptrac.PtracOption]) -> None:
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
                if isinstance(item, ptrac.PtracOption):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(ptrac.PtracOption.from_mcnp(item))
            options = types.Tuple(ptrac.PtracOption)(array)

        self._options: types.Tuple(ptrac.PtracOption) = options
