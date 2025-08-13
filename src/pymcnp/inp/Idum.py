import re

from . import _card
from .. import types
from .. import errors


class Idum(_card.Card):
    """
    Represents INP `idum` cards.
    """

    _KEYWORD = 'idum'

    _ATTRS = {
        'intergers': types.Tuple(types.Integer),
    }

    _REGEX = re.compile(rf'\Aidum((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)

    def __init__(self, intergers: list[str] | list[int] | list[types.Integer]):
        """
        Initializes `Idum`.

        Parameters:
            intergers: Integer array.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.intergers: types.Tuple(types.Integer) = intergers

    @property
    def intergers(self) -> types.Tuple(types.Integer):
        """
        Integer array

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._intergers

    @intergers.setter
    def intergers(self, intergers: list[str] | list[int] | list[types.Integer]) -> None:
        """
        Sets `intergers`.

        Parameters:
            intergers: Integer array.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if intergers is not None:
            array = []
            for item in intergers:
                if isinstance(item, types.Integer):
                    array.append(item)
                elif isinstance(item, int):
                    array.append(types.Integer(item))
                elif isinstance(item, str):
                    array.append(types.Integer.from_mcnp(item))
            intergers = types.Tuple(types.Integer)(array)

        if intergers is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, intergers)

        self._intergers: types.Tuple(types.Integer) = intergers
