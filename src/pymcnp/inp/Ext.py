import re

from . import _card
from .. import types
from .. import errors


class Ext(_card.Card):
    """
    Represents INP `ext` cards.
    """

    _KEYWORD = 'ext'

    _ATTRS = {
        'designator': types.Designator,
        'stretching': types.Tuple(types.String),
    }

    _REGEX = re.compile(rf'\Aext:(\S+)((?: {types.String._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)

    def __init__(self, designator: str | types.Designator, stretching: list[str] | list[types.String]):
        """
        Initializes `Ext`.

        Parameters:
            designator: Data card particle designator.
            stretching: Stretching direction for the cell.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.designator: types.Designator = designator
        self.stretching: types.Tuple(types.String) = stretching

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
    def stretching(self) -> types.Tuple(types.String):
        """
        Stretching direction for the cell

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._stretching

    @stretching.setter
    def stretching(self, stretching: list[str] | list[types.String]) -> None:
        """
        Sets `stretching`.

        Parameters:
            stretching: Stretching direction for the cell.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if stretching is not None:
            array = []
            for item in stretching:
                if isinstance(item, types.String):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(types.String.from_mcnp(item))
            stretching = types.Tuple(types.String)(array)

        if stretching is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, stretching)

        self._stretching: types.Tuple(types.String) = stretching
