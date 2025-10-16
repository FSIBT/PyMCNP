import re

from . import _card
from .. import types
from .. import errors


class Pwt(_card.Card):
    """
    Represents INP `pwt` cards.
    """

    _KEYWORD = 'pwt'

    _ATTRS = {
        'weights': types.Tuple(types.Real),
    }

    _REGEX = re.compile(rf'\Apwt((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)

    def __init__(self, weights: list[str] | list[float] | list[types.Real]):
        """
        Initializes `Pwt`.

        Parameters:
            weights: Relative threshold weight of photons produced at neutron collisions in cell.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.weights: types.Tuple(types.Real) = weights

    @property
    def weights(self) -> types.Tuple(types.Real):
        """
        Relative threshold weight of photons produced at neutron collisions in cell

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._weights

    @weights.setter
    def weights(self, weights: list[str] | list[float] | list[types.Real]) -> None:
        """
        Sets `weights`.

        Parameters:
            weights: Relative threshold weight of photons produced at neutron collisions in cell.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if weights is not None:
            array = []
            for item in weights:
                if isinstance(item, types.Real):
                    array.append(item)
                elif isinstance(item, int) or isinstance(item, float):
                    array.append(types.Real(item))
                elif isinstance(item, str):
                    array.append(types.Real.from_mcnp(item))
            weights = types.Tuple(types.Real)(array)

        if weights is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, weights)

        self._weights: types.Tuple(types.Real) = weights
