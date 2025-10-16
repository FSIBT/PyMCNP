import re

from . import _card
from .. import types
from .. import errors


class Area(_card.Card):
    """
    Represents INP area cards.
    """

    _KEYWORD = 'area'

    _ATTRS = {
        'areas': types.Tuple(types.Real),
    }

    _REGEX = re.compile(rf'\Aarea((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)

    def __init__(self, areas: list[str] | list[float] | list[types.Real]):
        """
        Initializes `Area`.

        Parameters:
            areas: Tuple of surface areas.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.areas: types.Tuple(types.Real) = areas

    @property
    def areas(self) -> types.Tuple(types.Real):
        """
        Tuple of surface areas

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._areas

    @areas.setter
    def areas(self, areas: list[str] | list[float] | list[types.Real]) -> None:
        """
        Sets `areas`.

        Parameters:
            areas: Tuple of surface areas.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if areas is not None:
            array = []
            for item in areas:
                if isinstance(item, types.Real):
                    array.append(item)
                elif isinstance(item, int) or isinstance(item, float):
                    array.append(types.Real(item))
                elif isinstance(item, str):
                    array.append(types.Real.from_mcnp(item))
            areas = types.Tuple(types.Real)(array)

        if areas is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, areas)

        self._areas: types.Tuple(types.Real) = areas
