import re

from . import _option
from ... import types
from ... import errors


class Freq(_option.MplotOption):
    """
    Represents INP `freq` elements.
    """

    _KEYWORD = 'freq'

    _ATTRS = {
        'n': types.Integer,
    }

    _REGEX = re.compile(rf'\Afreq( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, n: str | int | types.Integer):
        """
        Initializes `Freq`.

        Parameters:
            n: Number of histories between plotting calls.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.n: types.Integer = n

    @property
    def n(self) -> types.Integer:
        """
        Number of histories between plotting calls

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._n

    @n.setter
    def n(self, n: str | int | types.Integer) -> None:
        """
        Sets `n`.

        Parameters:
            n: Number of histories between plotting calls.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if n is not None:
            if isinstance(n, types.Integer):
                n = n
            elif isinstance(n, int):
                n = types.Integer(n)
            elif isinstance(n, str):
                n = types.Integer.from_mcnp(n)

        if n is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, n)

        self._n: types.Integer = n
