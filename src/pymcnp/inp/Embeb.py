import re

from . import _card
from .. import types
from .. import errors


class Embeb(_card.Card):
    """
    Represents INP `embeb` cards.
    """

    _KEYWORD = 'embeb'

    _ATTRS = {
        'suffix': types.Integer,
        'bounds': types.Tuple(types.Real),
    }

    _REGEX = re.compile(rf'\Aembeb(\d+)((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)

    def __init__(self, suffix: str | int | types.Integer, bounds: list[str] | list[float] | list[types.Real]):
        """
        Initializes `Embeb`.

        Parameters:
            suffix: Data card option suffix.
            bounds: Tuple of upper energy bounds.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.suffix: types.Integer = suffix
        self.bounds: types.Tuple(types.Real) = bounds

    @property
    def suffix(self) -> types.Integer:
        """
        Data card option suffix

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._suffix

    @suffix.setter
    def suffix(self, suffix: str | int | types.Integer) -> None:
        """
        Sets `suffix`.

        Parameters:
            suffix: Data card option suffix.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if suffix is not None:
            if isinstance(suffix, types.Integer):
                suffix = suffix
            elif isinstance(suffix, int):
                suffix = types.Integer(suffix)
            elif isinstance(suffix, str):
                suffix = types.Integer.from_mcnp(suffix)

        if suffix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, suffix)

        self._suffix: types.Integer = suffix

    @property
    def bounds(self) -> types.Tuple(types.Real):
        """
        Tuple of upper energy bounds

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
            bounds: Tuple of upper energy bounds.

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
