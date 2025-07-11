import re

from . import ptrac
from . import _option
from ...utils import types


class Ptrac(_option.DataOption):
    """
    Represents INP ptrac elements.

    Attributes:
        options: Dictionary of options.
    """

    _KEYWORD = 'ptrac'

    _ATTRS = {
        'options': types.Tuple[ptrac.PtracOption],
    }

    _REGEX = re.compile(rf'\Aptrac((?: (?:{ptrac.PtracOption._REGEX.pattern[2:-2]}))+?)?\Z')

    def __init__(self, options: list[str] | list[ptrac.PtracOption] = None):
        """
        Initializes ``Ptrac``.

        Parameters:
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.options: types.Tuple[ptrac.PtracOption] = options

    @property
    def options(self) -> types.Tuple[ptrac.PtracOption]:
        """
        Gets ``options``.

        Returns:
            ``options``.
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
                else:
                    raise TypeError
            options = types.Tuple(array)

        self._options: types.Tuple[ptrac.PtracOption] = options
