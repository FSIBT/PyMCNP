import re

from . import _card
from .. import types
from .. import errors


class Elpt(_card.Card):
    """
    Represents INP `elpt` cards.
    """

    _KEYWORD = 'elpt'

    _ATTRS = {
        'cutoffs': types.Tuple(types.Real),
    }

    _REGEX = re.compile(rf'\Aelpt((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)

    def __init__(self, cutoffs: list[str] | list[float] | list[types.Real]):
        """
        Initializes `Elpt`.

        Parameters:
            cutoffs: Tuple of cell lower energy cutoffs.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.cutoffs: types.Tuple(types.Real) = cutoffs

    @property
    def cutoffs(self) -> types.Tuple(types.Real):
        """
        Tuple of cell lower energy cutoffs

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._cutoffs

    @cutoffs.setter
    def cutoffs(self, cutoffs: list[str] | list[float] | list[types.Real]) -> None:
        """
        Sets `cutoffs`.

        Parameters:
            cutoffs: Tuple of cell lower energy cutoffs.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if cutoffs is not None:
            array = []
            for item in cutoffs:
                if isinstance(item, types.Real):
                    array.append(item)
                elif isinstance(item, int) or isinstance(item, float):
                    array.append(types.Real(item))
                elif isinstance(item, str):
                    array.append(types.Real.from_mcnp(item))
            cutoffs = types.Tuple(types.Real)(array)

        if cutoffs is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, cutoffs)

        self._cutoffs: types.Tuple(types.Real) = cutoffs
