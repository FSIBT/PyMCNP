import re

from . import _option
from ... import types
from ... import errors


class Tfc(_option.MplotOption):
    """
    Represents INP `tfc` elements.
    """

    _KEYWORD = 'tfc'

    _ATTRS = {
        'x': types.String,
    }

    _REGEX = re.compile(rf'\Atfc( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, x: str | types.String):
        """
        Initializes `Tfc`.

        Parameters:
            x: Independent variable selector.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.x: types.String = x

    @property
    def x(self) -> types.String:
        """
        Independent variable selector

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
            x: Independent variable selector.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if x is not None:
            if isinstance(x, types.String):
                x = x
            elif isinstance(x, str):
                x = types.String.from_mcnp(x)

        if x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x)

        self._x: types.String = x
