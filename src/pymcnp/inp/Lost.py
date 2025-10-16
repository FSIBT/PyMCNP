import re

from . import _card
from .. import types
from .. import errors


class Lost(_card.Card):
    """
    Represents INP `lost` cards.
    """

    _KEYWORD = 'lost'

    _ATTRS = {
        'lost1': types.Integer,
        'lost2': types.Integer,
    }

    _REGEX = re.compile(rf'\Alost( {types.Integer._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, lost1: str | int | types.Integer, lost2: str | int | types.Integer):
        """
        Initializes `Lost`.

        Parameters:
            lost1: Number of particles which can be lost before job termination.
            lost2: Maximum number of debug prints for lost particles..

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.lost1: types.Integer = lost1
        self.lost2: types.Integer = lost2

    @property
    def lost1(self) -> types.Integer:
        """
        Number of particles which can be lost before job termination

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._lost1

    @lost1.setter
    def lost1(self, lost1: str | int | types.Integer) -> None:
        """
        Sets `lost1`.

        Parameters:
            lost1: Number of particles which can be lost before job termination.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if lost1 is not None:
            if isinstance(lost1, types.Integer):
                lost1 = lost1
            elif isinstance(lost1, int):
                lost1 = types.Integer(lost1)
            elif isinstance(lost1, str):
                lost1 = types.Integer.from_mcnp(lost1)

        if lost1 is None or not (lost1 >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, lost1)

        self._lost1: types.Integer = lost1

    @property
    def lost2(self) -> types.Integer:
        """
        Maximum number of debug prints for lost particles.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._lost2

    @lost2.setter
    def lost2(self, lost2: str | int | types.Integer) -> None:
        """
        Sets `lost2`.

        Parameters:
            lost2: Maximum number of debug prints for lost particles..

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if lost2 is not None:
            if isinstance(lost2, types.Integer):
                lost2 = lost2
            elif isinstance(lost2, int):
                lost2 = types.Integer(lost2)
            elif isinstance(lost2, str):
                lost2 = types.Integer.from_mcnp(lost2)

        if lost2 is None or not (lost2 >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, lost2)

        self._lost2: types.Integer = lost2
