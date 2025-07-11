import re

from . import sdef
from . import _option
from ...utils import types


class Sdef(_option.DataOption):
    """
    Represents INP sdef elements.

    Attributes:
        options: Dictionary of options.
    """

    _KEYWORD = 'sdef'

    _ATTRS = {
        'options': types.Tuple[sdef.SdefOption],
    }

    _REGEX = re.compile(rf'\Asdef((?: (?:{sdef.SdefOption._REGEX.pattern[2:-2]}))+?)?\Z')

    def __init__(self, options: list[str] | list[sdef.SdefOption] = None):
        """
        Initializes ``Sdef``.

        Parameters:
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.options: types.Tuple[sdef.SdefOption] = options

    @property
    def options(self) -> types.Tuple[sdef.SdefOption]:
        """
        Gets ``options``.

        Returns:
            ``options``.
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
                else:
                    raise TypeError
            options = types.Tuple(array)

        self._options: types.Tuple[sdef.SdefOption] = options
