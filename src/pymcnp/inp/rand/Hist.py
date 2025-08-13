import re

from . import _option
from ... import types
from ... import errors


class Hist(_option.RandOption):
    """
    Represents INP `hist` elements.
    """

    _KEYWORD = 'hist'

    _ATTRS = {
        'hist': types.Integer,
    }

    _REGEX = re.compile(rf'\Ahist( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, hist: str | int | types.Integer):
        """
        Initializes `Hist`.

        Parameters:
            hist: Starting pseudorandom number.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.hist: types.Integer = hist

    @property
    def hist(self) -> types.Integer:
        """
        Starting pseudorandom number

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._hist

    @hist.setter
    def hist(self, hist: str | int | types.Integer) -> None:
        """
        Sets `hist`.

        Parameters:
            hist: Starting pseudorandom number.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if hist is not None:
            if isinstance(hist, types.Integer):
                hist = hist
            elif isinstance(hist, int):
                hist = types.Integer(hist)
            elif isinstance(hist, str):
                hist = types.Integer.from_mcnp(hist)

        if hist is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, hist)

        self._hist: types.Integer = hist
