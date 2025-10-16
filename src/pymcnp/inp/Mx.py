import re

from . import _card
from .. import types
from .. import errors


class Mx(_card.Card):
    """
    Represents INP `mx` cards.
    """

    _KEYWORD = 'mx'

    _ATTRS = {
        'suffix': types.Integer,
        'designator': types.Designator,
        'zaids': types.Tuple(types.String),
    }

    _REGEX = re.compile(rf'\Amx(\d+):(\S+)((?: (?:{types.Zaid._REGEX.pattern[2:-2]}|j|model|0))+?)\Z', re.IGNORECASE)

    def __init__(self, suffix: str | int | types.Integer, designator: str | types.Designator, zaids: list[str] | list[types.String]):
        """
        Initializes `Mx`.

        Parameters:
            suffix: Data card option suffix.
            designator: Data card particle designator.
            zaids: Zaid substitutions for particles.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.suffix: types.Integer = suffix
        self.designator: types.Designator = designator
        self.zaids: types.Tuple(types.String) = zaids

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
    def designator(self) -> types.Designator:
        """
        Data card particle designator

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._designator

    @designator.setter
    def designator(self, designator: str | types.Designator) -> None:
        """
        Sets `designator`.

        Parameters:
            designator: Data card particle designator.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if designator is not None:
            if isinstance(designator, types.Designator):
                designator = designator
            elif isinstance(designator, str):
                designator = types.Designator.from_mcnp(designator)

        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, designator)

        self._designator: types.Designator = designator

    @property
    def zaids(self) -> types.Tuple(types.String):
        """
        Zaid substitutions for particles

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._zaids

    @zaids.setter
    def zaids(self, zaids: list[str] | list[types.String]) -> None:
        """
        Sets `zaids`.

        Parameters:
            zaids: Zaid substitutions for particles.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if zaids is not None:
            array = []
            for item in zaids:
                if isinstance(item, types.String):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(types.String.from_mcnp(item))
            zaids = types.Tuple(types.String)(array)

        if zaids is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, zaids)

        self._zaids: types.Tuple(types.String) = zaids
