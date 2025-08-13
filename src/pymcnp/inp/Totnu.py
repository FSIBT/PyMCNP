import re

from . import _card
from .. import types
from .. import errors


class Totnu(_card.Card):
    """
    Represents INP `totnu` cards.
    """

    _KEYWORD = 'totnu'

    _ATTRS = {
        'no': types.String,
    }

    _REGEX = re.compile(rf'\Atotnu( {types.String._REGEX.pattern[2:-2]})?\Z', re.IGNORECASE)

    def __init__(self, no: str | types.String = None):
        """
        Initializes `Totnu`.

        Parameters:
            no: Delay fission sampling on/off.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.no: types.String = no

    @property
    def no(self) -> types.String:
        """
        Delay fission sampling on/off

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._no

    @no.setter
    def no(self, no: str | types.String) -> None:
        """
        Sets `no`.

        Parameters:
            no: Delay fission sampling on/off.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if no is not None:
            if isinstance(no, types.String):
                no = no
            elif isinstance(no, str):
                no = types.String.from_mcnp(no)

        if no is not None and not (no == 'no'):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, no)

        self._no: types.String = no
