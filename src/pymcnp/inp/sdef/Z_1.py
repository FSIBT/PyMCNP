import re

from . import _option
from ... import types
from ... import errors


class Z_1(_option.SdefOption):
    """
    Represents INP `z` elements variation #1.
    """

    _KEYWORD = 'z'

    _ATTRS = {
        'position': types.Distribution,
    }

    _REGEX = re.compile(rf'\Az( {types.Distribution._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, position: str | types.Distribution):
        """
        Initializes `Z_1`.

        Parameters:
            position: Position z-component.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.position: types.Distribution = position

    @property
    def position(self) -> types.Distribution:
        """
        Position z-component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._position

    @position.setter
    def position(self, position: str | types.Distribution) -> None:
        """
        Sets `position`.

        Parameters:
            position: Position z-component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if position is not None:
            if isinstance(position, types.Distribution):
                position = position
            elif isinstance(position, str):
                position = types.Distribution.from_mcnp(position)

        if position is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, position)

        self._position: types.Distribution = position
