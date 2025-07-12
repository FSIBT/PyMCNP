import re

from . import var
from . import _option
from ...utils import types


class Var(_option.DataOption):
    """
    Represents INP var elements.
    """

    _KEYWORD = 'var'

    _ATTRS = {
        'options': types.Tuple[var.VarOption],
    }

    _REGEX = re.compile(rf'\Avar((?: (?:{var.VarOption._REGEX.pattern[2:-2]}))+?)?\Z')

    def __init__(self, options: list[str] | list[var.VarOption] = None):
        """
        Initializes ``Var``.

        Parameters:
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.options: types.Tuple[var.VarOption] = options

    @property
    def options(self) -> types.Tuple[var.VarOption]:
        """
        Dictionary of options

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._options

    @options.setter
    def options(self, options: list[str] | list[var.VarOption]) -> None:
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
                if isinstance(item, var.VarOption):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(var.VarOption.from_mcnp(item))

            options = types.Tuple(array)

        self._options: types.Tuple[var.VarOption] = options
