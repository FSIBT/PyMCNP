import re

from . import dawwg
from . import _option
from ...utils import types


class Dawwg(_option.DataOption):
    """
    Represents INP dawwg elements.
    """

    _KEYWORD = 'dawwg'

    _ATTRS = {
        'options': types.Tuple[dawwg.DawwgOption],
    }

    _REGEX = re.compile(rf'\Adawwg((?: (?:{dawwg.DawwgOption._REGEX.pattern[2:-2]}))+?)?\Z')

    def __init__(self, options: list[str] | list[dawwg.DawwgOption] = None):
        """
        Initializes ``Dawwg``.

        Parameters:
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.options: types.Tuple[dawwg.DawwgOption] = options

    @property
    def options(self) -> types.Tuple[dawwg.DawwgOption]:
        """
        Dictionary of options

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._options

    @options.setter
    def options(self, options: list[str] | list[dawwg.DawwgOption]) -> None:
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
                if isinstance(item, dawwg.DawwgOption):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(dawwg.DawwgOption.from_mcnp(item))
            options = types.Tuple(array)

        self._options: types.Tuple[dawwg.DawwgOption] = options
