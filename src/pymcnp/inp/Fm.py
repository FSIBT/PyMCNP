import re

from . import _card
from .. import types
from .. import errors


class Fm(_card.Card):
    """
    Represents INP `fm` cards.
    """

    _KEYWORD = 'fm'

    _ATTRS = {
        'prefix': types.String,
        'suffix': types.Integer,
        'bins': types.String,
    }

    _REGEX = re.compile(r'\A([+*])?fm(\d+)( [\S\s]+)\Z', re.IGNORECASE)

    def __init__(self, suffix: str | int | types.Integer, bins: str | types.String, prefix: str | types.String = None):
        """
        Initializes `Fm`.

        Parameters:
            prefix: Star prefix.
            suffix: Data card option suffix.
            bins: Tally multiplier bins.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.prefix: types.String = prefix
        self.suffix: types.Integer = suffix
        self.bins: types.String = bins

    @property
    def prefix(self) -> types.String:
        """
        Star prefix

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._prefix

    @prefix.setter
    def prefix(self, prefix: str | types.String) -> None:
        """
        Sets `prefix`.

        Parameters:
            prefix: Star prefix.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if prefix is not None:
            if isinstance(prefix, types.String):
                prefix = prefix
            elif isinstance(prefix, str):
                prefix = types.String.from_mcnp(prefix)

        if prefix is not None and prefix.value.lower() not in {'*', '+'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, prefix)

        self._prefix: types.String = prefix

    @property
    def suffix(self) -> types.Integer:
        """
        Data card option suffix

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._suffix

    @suffix.setter
    def suffix(self, suffix: str | int | types.Integer) -> None:
        """
        Sets `suffix`.

        Parameters:
            suffix: Data card option suffix.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if suffix is not None:
            if isinstance(suffix, types.Integer):
                suffix = suffix
            elif isinstance(suffix, int):
                suffix = types.Integer(suffix)
            elif isinstance(suffix, str):
                suffix = types.Integer.from_mcnp(suffix)

        if suffix is None or not (suffix <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, suffix)

        self._suffix: types.Integer = suffix

    @property
    def bins(self) -> types.String:
        """
        Tally multiplier bins

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._bins

    @bins.setter
    def bins(self, bins: str | types.String) -> None:
        """
        Sets `bins`.

        Parameters:
            bins: Tally multiplier bins.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if bins is not None:
            if isinstance(bins, types.String):
                bins = bins
            elif isinstance(bins, str):
                bins = types.String.from_mcnp(bins)

        if bins is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, bins)

        self._bins: types.String = bins
