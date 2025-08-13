import re

from . import _option
from ... import types
from ... import errors


class Zlev(_option.MplotOption):
    """
    Represents INP `zlev` elements.
    """

    _KEYWORD = 'zlev'

    _ATTRS = {
        'n': types.Tuple(types.String),
    }

    _REGEX = re.compile(rf'\Azlev((?: {types.String._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)

    def __init__(self, n: list[str] | list[types.String]):
        """
        Initializes `Zlev`.

        Parameters:
            n: Scales of tally plots.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.n: types.Tuple(types.String) = n

    @property
    def n(self) -> types.Tuple(types.String):
        """
        Scales of tally plots

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._n

    @n.setter
    def n(self, n: list[str] | list[types.String]) -> None:
        """
        Sets `n`.

        Parameters:
            n: Scales of tally plots.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if n is not None:
            array = []
            for item in n:
                if isinstance(item, types.String):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(types.String.from_mcnp(item))
            n = types.Tuple(types.String)(array)

        if n is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, n)

        self._n: types.Tuple(types.String) = n
