import re

from . import _card
from .. import types
from .. import errors


class Wwt(_card.Card):
    """
    Represents INP `wwt` cards.
    """

    _KEYWORD = 'wwt'

    _ATTRS = {
        'designator': types.Designator,
        'bounds': types.Tuple(types.Real),
    }

    _REGEX = re.compile(rf'\Awwt:(\S+)((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)

    def __init__(self, designator: str | types.Designator, bounds: list[str] | list[float] | list[types.Real]):
        """
        Initializes `Wwt`.

        Parameters:
            designator: Data card particle designator.
            bounds: Upper time bound.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.designator: types.Designator = designator
        self.bounds: types.Tuple(types.Real) = bounds

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
    def bounds(self) -> types.Tuple(types.Real):
        """
        Upper time bound

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._bounds

    @bounds.setter
    def bounds(self, bounds: list[str] | list[float] | list[types.Real]) -> None:
        """
        Sets `bounds`.

        Parameters:
            bounds: Upper time bound.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if bounds is not None:
            array = []
            for item in bounds:
                if isinstance(item, types.Real):
                    array.append(item)
                elif isinstance(item, int) or isinstance(item, float):
                    array.append(types.Real(item))
                elif isinstance(item, str):
                    array.append(types.Real.from_mcnp(item))
            bounds = types.Tuple(types.Real)(array)

        if bounds is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, bounds)

        self._bounds: types.Tuple(types.Real) = bounds
