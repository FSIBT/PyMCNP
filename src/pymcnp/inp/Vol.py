import re

from . import _card
from .. import types
from .. import errors


class Vol(_card.Card):
    """
    Represents INP `vol` cards.
    """

    _KEYWORD = 'vol'

    _ATTRS = {
        'no': types.String,
        'volumes': types.Tuple(types.Real),
    }

    _REGEX = re.compile(rf'\Avol(?: (no))?((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)

    def __init__(self, volumes: list[str] | list[float] | list[types.Real], no: str | types.String = None):
        """
        Initializes `Vol`.

        Parameters:
            no: Volume calculation on/off.
            volumes: Tuple of cell volumes.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.no: types.String = no
        self.volumes: types.Tuple(types.Real) = volumes

    @property
    def no(self) -> types.String:
        """
        Volume calculation on/off

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
            no: Volume calculation on/off.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if no is not None:
            if isinstance(no, types.String):
                no = no
            elif isinstance(no, str):
                no = types.String.from_mcnp(no)

        if no is not None and no.value.lower() not in {'no'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, no)

        self._no: types.String = no

    @property
    def volumes(self) -> types.Tuple(types.Real):
        """
        Tuple of cell volumes

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._volumes

    @volumes.setter
    def volumes(self, volumes: list[str] | list[float] | list[types.Real]) -> None:
        """
        Sets `volumes`.

        Parameters:
            volumes: Tuple of cell volumes.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if volumes is not None:
            array = []
            for item in volumes:
                if isinstance(item, types.Real):
                    array.append(item)
                elif isinstance(item, int) or isinstance(item, float):
                    array.append(types.Real(item))
                elif isinstance(item, str):
                    array.append(types.Real.from_mcnp(item))
            volumes = types.Tuple(types.Real)(array)

        if volumes is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, volumes)

        self._volumes: types.Tuple(types.Real) = volumes
