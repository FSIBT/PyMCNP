import re

from . import _option
from ... import types
from ... import errors


class Ic(_option.DfOption_1):
    """
    Represents INP `ic` elements.
    """

    _KEYWORD = 'ic'

    _ATTRS = {
        'function': types.Integer,
    }

    _REGEX = re.compile(rf'\Aic( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, function: str | int | types.Integer):
        """
        Initializes `Ic`.

        Parameters:
            function: Standard dose function.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.function: types.Integer = function

    @property
    def function(self) -> types.Integer:
        """
        Standard dose function

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._function

    @function.setter
    def function(self, function: str | int | types.Integer) -> None:
        """
        Sets `function`.

        Parameters:
            function: Standard dose function.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if function is not None:
            if isinstance(function, types.Integer):
                function = function
            elif isinstance(function, int):
                function = types.Integer(function)
            elif isinstance(function, str):
                function = types.Integer.from_mcnp(function)

        if function is None or not (isinstance(function.value, types.Jump) or function in {10, 20, 31, 32, 33, 34, 35, 40, 99}):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, function)

        self._function: types.Integer = function
