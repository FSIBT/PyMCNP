import re

from . import _option
from ...utils import types
from ...utils import errors


class Area(_option.DataOption):
    """
    Represents INP area elements.

    Attributes:
        areas: Tuple of surface areas.
    """

    _KEYWORD = 'area'

    _ATTRS = {
        'areas': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Aarea((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, areas: list[str] | list[float] | list[types.Real]):
        """
        Initializes ``Area``.

        Parameters:
            areas: Tuple of surface areas.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.areas: types.Tuple[types.Real] = areas

    @property
    def areas(self) -> types.Tuple[types.Real]:
        """
        Gets ``areas``.

        Returns:
            ``areas``.
        """

        return self._areas

    @areas.setter
    def areas(self, areas: list[str] | list[float] | list[types.Real]) -> None:
        """
        Sets ``areas``.

        Parameters:
            areas: Tuple of surface areas.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if areas is not None:
            array = []
            for item in areas:
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
            areas = types.Tuple(array)

        if areas is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, areas)

        self._areas: types.Tuple[types.Real] = areas
