import re

from . import _option
from ... import types
from ... import errors


class Rdum(_option.DataOption):
    """
    Represents INP rdum elements.
    """

    _KEYWORD = 'rdum'

    _ATTRS = {
        'floats': types.Tuple(types.Real),
    }

    _REGEX = re.compile(rf'\Ardum((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, floats: list[str] | list[float] | list[types.Real]):
        """
        Initializes ``Rdum``.

        Parameters:
            floats: Floating point array.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.floats: types.Tuple(types.Real) = floats

    @property
    def floats(self) -> types.Tuple(types.Real):
        """
        Floating point array

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._floats

    @floats.setter
    def floats(self, floats: list[str] | list[float] | list[types.Real]) -> None:
        """
        Sets ``floats``.

        Parameters:
            floats: Floating point array.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if floats is not None:
            array = []
            for item in floats:
                if isinstance(item, types.Real):
                    array.append(item)
                elif isinstance(item, int) or isinstance(item, float):
                    array.append(types.Real(item))
                elif isinstance(item, str):
                    array.append(types.Real.from_mcnp(item))
            floats = types.Tuple(types.Real)(array)

        if floats is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, floats)

        self._floats: types.Tuple(types.Real) = floats
