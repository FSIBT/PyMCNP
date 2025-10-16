import re

from . import free
from . import _option
from ... import types
from ... import errors


class Free(_option.MplotOption):
    """
    Represents INP `free` elements.
    """

    _KEYWORD = 'free'

    _ATTRS = {
        'x': types.String,
        'y': types.String,
        'option': free.FreeOption,
    }

    _REGEX = re.compile(rf'\Afree( {types.String._REGEX.pattern[2:-2]})( {types.String._REGEX.pattern[2:-2]})( (?:{free.FreeOption._REGEX.pattern[2:-2]}))?\Z', re.IGNORECASE)

    def __init__(self, x: str | types.String, y: str | types.String, option: str | free.FreeOption = None):
        """
        Initializes `Free`.

        Parameters:
            x: Independent variable.
            y: Dependent variable.
            option: free option.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.x: types.String = x
        self.y: types.String = y
        self.option: free.FreeOption = option

    @property
    def x(self) -> types.String:
        """
        Independent variable

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._x

    @x.setter
    def x(self, x: str | types.String) -> None:
        """
        Sets `x`.

        Parameters:
            x: Independent variable.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if x is not None:
            if isinstance(x, types.String):
                x = x
            elif isinstance(x, str):
                x = types.String.from_mcnp(x)

        if x is None or x.value.lower() not in {'f', 'd', 'u', 's', 'm', 'c', 'e', 't', 'i', 'j', 'k'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x)

        self._x: types.String = x

    @property
    def y(self) -> types.String:
        """
        Dependent variable

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._y

    @y.setter
    def y(self, y: str | types.String) -> None:
        """
        Sets `y`.

        Parameters:
            y: Dependent variable.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if y is not None:
            if isinstance(y, types.String):
                y = y
            elif isinstance(y, str):
                y = types.String.from_mcnp(y)

        if y is None or y.value.lower() not in {'f', 'd', 'u', 's', 'm', 'c', 'e', 't', 'i', 'j', 'k'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, y)

        self._y: types.String = y

    @property
    def option(self) -> free.FreeOption:
        """
        Free option

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._option

    @option.setter
    def option(self, option: str | free.FreeOption) -> None:
        """
        Sets `option`.

        Parameters:
            option: free option.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if option is not None:
            if isinstance(option, free.FreeOption):
                option = option
            elif isinstance(option, str):
                option = free.FreeOption.from_mcnp(option)

        self._option: free.FreeOption = option
