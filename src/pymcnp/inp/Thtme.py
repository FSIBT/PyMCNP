import re

from . import _card
from .. import types
from .. import errors


class Thtme(_card.Card):
    """
    Represents INP `thtme` cards.
    """

    _KEYWORD = 'thtme'

    _ATTRS = {
        'times': types.Tuple(types.Real),
    }

    _REGEX = re.compile(rf'\Athtme((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)

    def __init__(self, times: list[str] | list[float] | list[types.Real]):
        """
        Initializes `Thtme`.

        Parameters:
            times: Tuple of times when thermal temperatures are specified.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.times: types.Tuple(types.Real) = times

    @property
    def times(self) -> types.Tuple(types.Real):
        """
        Tuple of times when thermal temperatures are specified

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._times

    @times.setter
    def times(self, times: list[str] | list[float] | list[types.Real]) -> None:
        """
        Sets `times`.

        Parameters:
            times: Tuple of times when thermal temperatures are specified.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if times is not None:
            array = []
            for item in times:
                if isinstance(item, types.Real):
                    array.append(item)
                elif isinstance(item, int) or isinstance(item, float):
                    array.append(types.Real(item))
                elif isinstance(item, str):
                    array.append(types.Real.from_mcnp(item))
            times = types.Tuple(types.Real)(array)

        if times is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, times)

        self._times: types.Tuple(types.Real) = times
