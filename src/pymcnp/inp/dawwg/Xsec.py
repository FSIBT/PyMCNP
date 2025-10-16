import re

from . import _option
from ... import types
from ... import errors


class Xsec(_option.DawwgOption):
    """
    Represents INP `xsec` elements.
    """

    _KEYWORD = 'xsec'

    _ATTRS = {
        'name': types.String,
    }

    _REGEX = re.compile(rf'\Axsec( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, name: str | types.String):
        """
        Initializes `Xsec`.

        Parameters:
            name: Cross section library.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.name: types.String = name

    @property
    def name(self) -> types.String:
        """
        Cross section library

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._name

    @name.setter
    def name(self, name: str | types.String) -> None:
        """
        Sets `name`.

        Parameters:
            name: Cross section library.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if name is not None:
            if isinstance(name, types.String):
                name = name
            elif isinstance(name, str):
                name = types.String.from_mcnp(name)

        if name is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, name)

        self._name: types.String = name
