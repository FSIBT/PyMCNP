import re

from . import _card
from .. import types
from .. import errors


class Otfdb(_card.Card):
    """
    Represents INP `otfdb` cards.
    """

    _KEYWORD = 'otfdb'

    _ATTRS = {
        'zaids': types.Tuple(types.Zaid),
    }

    _REGEX = re.compile(rf'\Aotfdb((?: {types.Zaid._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)

    def __init__(self, zaids: list[str] | list[types.Zaid]):
        """
        Initializes `Otfdb`.

        Parameters:
            zaids: Identifiers for the broadening tables.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.zaids: types.Tuple(types.Zaid) = zaids

    @property
    def zaids(self) -> types.Tuple(types.Zaid):
        """
        Identifiers for the broadening tables

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._zaids

    @zaids.setter
    def zaids(self, zaids: list[str] | list[types.Zaid]) -> None:
        """
        Sets `zaids`.

        Parameters:
            zaids: Identifiers for the broadening tables.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if zaids is not None:
            array = []
            for item in zaids:
                if isinstance(item, types.Zaid):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(types.Zaid.from_mcnp(item))
            zaids = types.Tuple(types.Zaid)(array)

        if zaids is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, zaids)

        self._zaids: types.Tuple(types.Zaid) = zaids
