import re

from . import _option
from ....utils import types
from ....utils import errors


class Rho(_option.KpertOption):
    """
    Represents INP rho elements.

    Attributes:
        densities: List of densities.
    """

    _KEYWORD = 'rho'

    _ATTRS = {
        'densities': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Arho((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, densities: list[str] | list[float] | list[types.Real]):
        """
        Initializes ``Rho``.

        Parameters:
            densities: List of densities.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.densities: types.Tuple[types.Real] = densities

    @property
    def densities(self) -> types.Tuple[types.Real]:
        """
        Gets ``densities``.

        Returns:
            ``densities``.
        """

        return self._densities

    @densities.setter
    def densities(self, densities: list[str] | list[float] | list[types.Real]) -> None:
        """
        Sets ``densities``.

        Parameters:
            densities: List of densities.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if densities is not None:
            array = []
            for item in densities:
                if isinstance(item, types.Real):
                    array.append(item)
                elif isinstance(item, int):
                    array.append(types.Real(item))
                elif isinstance(item, float):
                    array.append(types.Real(item))
                elif isinstance(item, str):
                    array.append(types.Real.from_mcnp(item))
                else:
                    raise TypeError
            densities = types.Tuple(array)

        if densities is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, densities)

        self._densities: types.Tuple[types.Real] = densities
