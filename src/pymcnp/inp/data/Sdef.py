import re

from . import sdef
from . import _option
from ... import types


class Sdef(_option.DataOption):
    """
    Represents INP sdef elements.
    """

    _KEYWORD = 'sdef'

    _ATTRS = {
        'options': types.Tuple(sdef.SdefOption),
    }

    _REGEX = re.compile(rf'\Asdef((?: (?:{sdef.SdefOption._REGEX.pattern[2:-2]}))+?)?\Z', re.IGNORECASE)

    def __init__(self, options: list[str] | list[sdef.SdefOption] = None):
        """
        Initializes ``Sdef``.

        Parameters:
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.options: types.Tuple(sdef.SdefOption) = options

    @property
    def options(self) -> types.Tuple(sdef.SdefOption):
        """
        Dictionary of options

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._options

    @options.setter
    def options(self, options: list[str] | list[sdef.SdefOption]) -> None:
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
                if isinstance(item, sdef.SdefOption):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(sdef.SdefOption.from_mcnp(item))
            options = types.Tuple(sdef.SdefOption)(array)

        self._options: types.Tuple(sdef.SdefOption) = options
