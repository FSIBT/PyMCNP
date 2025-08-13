import re

from . import _option
from ... import types
from ... import errors


class Axs(_option.SsrOption):
    """
    Represents INP `axs` elements.
    """

    _KEYWORD = 'axs'

    _ATTRS = {
        'cosines': types.Tuple(types.Real),
    }

    _REGEX = re.compile(rf'\Aaxs((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)

    def __init__(self, cosines: list[str] | list[float] | list[types.Real]):
        """
        Initializes `Axs`.

        Parameters:
            cosines: Direction cosines defining.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.cosines: types.Tuple(types.Real) = cosines

    @property
    def cosines(self) -> types.Tuple(types.Real):
        """
        Direction cosines defining

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._cosines

    @cosines.setter
    def cosines(self, cosines: list[str] | list[float] | list[types.Real]) -> None:
        """
        Sets `cosines`.

        Parameters:
            cosines: Direction cosines defining.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if cosines is not None:
            array = []
            for item in cosines:
                if isinstance(item, types.Real):
                    array.append(item)
                elif isinstance(item, int) or isinstance(item, float):
                    array.append(types.Real(item))
                elif isinstance(item, str):
                    array.append(types.Real.from_mcnp(item))
            cosines = types.Tuple(types.Real)(array)

        if cosines is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, cosines)

        self._cosines: types.Tuple(types.Real) = cosines
