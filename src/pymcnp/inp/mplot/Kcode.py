import re

from . import _option
from ... import types
from ... import errors


class Kcode(_option.MplotOption):
    """
    Represents INP `kcode` elements.
    """

    _KEYWORD = 'kcode'

    _ATTRS = {
        'i': types.Integer,
    }

    _REGEX = re.compile(rf'\Akcode( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, i: str | int | types.Integer):
        """
        Initializes `Kcode`.

        Parameters:
            i: Lifetime to remove.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.i: types.Integer = i

    @property
    def i(self) -> types.Integer:
        """
        Lifetime to remove

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._i

    @i.setter
    def i(self, i: str | int | types.Integer) -> None:
        """
        Sets `i`.

        Parameters:
            i: Lifetime to remove.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if i is not None:
            if isinstance(i, types.Integer):
                i = i
            elif isinstance(i, int):
                i = types.Integer(i)
            elif isinstance(i, str):
                i = types.Integer.from_mcnp(i)

        if i is None or not ((i >= 1 and i <= 6) or (i >= 1 and i <= 19)):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, i)

        self._i: types.Integer = i
