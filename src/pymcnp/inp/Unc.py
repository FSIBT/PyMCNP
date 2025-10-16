import re

from . import _card
from .. import types
from .. import errors


class Unc(_card.Card):
    """
    Represents INP `unc` cards.
    """

    _KEYWORD = 'unc'

    _ATTRS = {
        'designator': types.Designator,
        'settings': types.Tuple(types.Integer),
    }

    _REGEX = re.compile(rf'\Aunc:(\S+)((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)

    def __init__(self, designator: str | types.Designator, settings: list[str] | list[int] | list[types.Integer]):
        """
        Initializes `Unc`.

        Parameters:
            designator: Data option particle designator.
            settings: Tuple of uncollided secondary settings.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.designator: types.Designator = designator
        self.settings: types.Tuple(types.Integer) = settings

    @property
    def designator(self) -> types.Designator:
        """
        Data option particle designator

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
            designator: Data option particle designator.

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
    def settings(self) -> types.Tuple(types.Integer):
        """
        Tuple of uncollided secondary settings

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._settings

    @settings.setter
    def settings(self, settings: list[str] | list[int] | list[types.Integer]) -> None:
        """
        Sets `settings`.

        Parameters:
            settings: Tuple of uncollided secondary settings.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if settings is not None:
            array = []
            for item in settings:
                if isinstance(item, types.Integer):
                    array.append(item)
                elif isinstance(item, int):
                    array.append(types.Integer(item))
                elif isinstance(item, str):
                    array.append(types.Integer.from_mcnp(item))
            settings = types.Tuple(types.Integer)(array)

        if settings is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, settings)

        self._settings: types.Tuple(types.Integer) = settings
