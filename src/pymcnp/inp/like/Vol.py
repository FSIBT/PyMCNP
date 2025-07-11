import re

from . import _option
from ...utils import types
from ...utils import errors


class Vol(_option.LikeOption):
    """
    Represents INP vol elements.

    Attributes:
        volume: Cell volume.
    """

    _KEYWORD = 'vol'

    _ATTRS = {
        'volume': types.Real,
    }

    _REGEX = re.compile(rf'\Avol( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, volume: str | int | float | types.Real):
        """
        Initializes ``Vol``.

        Parameters:
            volume: Cell volume.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.volume: types.Real = volume

    @property
    def volume(self) -> types.Real:
        """
        Gets ``volume``.

        Returns:
            ``volume``.
        """

        return self._volume

    @volume.setter
    def volume(self, volume: str | int | float | types.Real) -> None:
        """
        Sets ``volume``.

        Parameters:
            volume: Cell volume.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if volume is not None:
            if isinstance(volume, types.Real):
                volume = volume
            elif isinstance(volume, int):
                volume = types.Real(volume)
            elif isinstance(volume, float):
                volume = types.Real(volume)
            elif isinstance(volume, str):
                volume = types.Real.from_mcnp(volume)
            else:
                raise TypeError

        if volume is None or not (volume >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, volume)

        self._volume: types.Real = volume
