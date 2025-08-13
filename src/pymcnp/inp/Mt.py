import re

from . import _card
from .. import types
from .. import errors


class Mt(_card.Card):
    """
    Represents INP `mt` cards.
    """

    _KEYWORD = 'mt'

    _ATTRS = {
        'suffix': types.Integer,
        'identifiers': types.Tuple(types.String),
    }

    _REGEX = re.compile(rf'\Amt(\d+)((?: {types.String._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)

    def __init__(self, suffix: str | int | types.Integer, identifiers: list[str] | list[types.String]):
        """
        Initializes `Mt`.

        Parameters:
            suffix: Data card option suffix.
            identifiers: Corresponding S(α,β) identifier.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.suffix: types.Integer = suffix
        self.identifiers: types.Tuple(types.String) = identifiers

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

        if suffix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, suffix)

        self._suffix: types.Integer = suffix

    @property
    def identifiers(self) -> types.Tuple(types.String):
        """
        Corresponding S(α,β) identifier

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._identifiers

    @identifiers.setter
    def identifiers(self, identifiers: list[str] | list[types.String]) -> None:
        """
        Sets `identifiers`.

        Parameters:
            identifiers: Corresponding S(α,β) identifier.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if identifiers is not None:
            array = []
            for item in identifiers:
                if isinstance(item, types.String):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(types.String.from_mcnp(item))
            identifiers = types.Tuple(types.String)(array)

        if identifiers is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, identifiers)

        self._identifiers: types.Tuple(types.String) = identifiers
