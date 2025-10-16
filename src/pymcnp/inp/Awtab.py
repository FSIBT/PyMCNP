import re

from . import _card
from .. import types
from .. import errors


class Awtab(_card.Card):
    """
    Represents INP awtab cards.
    """

    _KEYWORD = 'awtab'

    _ATTRS = {
        'weight_ratios': types.Tuple(types.Substance),
    }

    _REGEX = re.compile(rf'\Aawtab((?: {types.Substance._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)

    def __init__(self, weight_ratios: list[str] | list[types.Substance]):
        """
        Initializes `Awtab`.

        Parameters:
            weight_ratios: Tuple of atomic weight ratios.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.weight_ratios: types.Tuple(types.Substance) = weight_ratios

    @property
    def weight_ratios(self) -> types.Tuple(types.Substance):
        """
        Tuple of atomic weight ratios

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._weight_ratios

    @weight_ratios.setter
    def weight_ratios(self, weight_ratios: list[str] | list[types.Substance]) -> None:
        """
        Sets `weight_ratios`.

        Parameters:
            weight_ratios: Tuple of atomic weight ratios.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if weight_ratios is not None:
            array = []
            for item in weight_ratios:
                if isinstance(item, types.Substance):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(types.Substance.from_mcnp(item))
            weight_ratios = types.Tuple(types.Substance)(array)

        if weight_ratios is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, weight_ratios)

        self._weight_ratios: types.Tuple(types.Substance) = weight_ratios
