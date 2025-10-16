import re

from . import _option
from ... import types
from ... import errors


class Y_0(_option.SdefOption):
    """
    Represents INP `y` elements variation #0.
    """

    _KEYWORD = 'y'

    _ATTRS = {
        'position': types.Real,
    }

    _REGEX = re.compile(rf'\Ay( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, position: str | int | float | types.Real):
        """
        Initializes `Y_0`.

        Parameters:
            position: Position y-component.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.position: types.Real = position

    @property
    def position(self) -> types.Real:
        """
        Position y-component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._position

    @position.setter
    def position(self, position: str | int | float | types.Real) -> None:
        """
        Sets `position`.

        Parameters:
            position: Position y-component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if position is not None:
            if isinstance(position, types.Real):
                position = position
            elif isinstance(position, int) or isinstance(position, float):
                position = types.Real(position)
            elif isinstance(position, str):
                position = types.Real.from_mcnp(position)

        if position is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, position)

        self._position: types.Real = position
