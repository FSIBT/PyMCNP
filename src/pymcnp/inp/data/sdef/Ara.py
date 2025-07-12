import re

from . import _option
from ....utils import types
from ....utils import errors


class Ara(_option.SdefOption):
    """
    Represents INP ara elements.
    """

    _KEYWORD = 'ara'

    _ATTRS = {
        'area': types.Real,
    }

    _REGEX = re.compile(rf'\Aara( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, area: str | int | float | types.Real):
        """
        Initializes ``Ara``.

        Parameters:
            area: Area of surface.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.area: types.Real = area

    @property
    def area(self) -> types.Real:
        """
        Area of surface

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._area

    @area.setter
    def area(self, area: str | int | float | types.Real) -> None:
        """
        Sets ``area``.

        Parameters:
            area: Area of surface.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if area is not None:
            if isinstance(area, types.Real):
                area = area
            elif isinstance(area, int) or isinstance(area, float):
                area = types.Real(area)
            elif isinstance(area, str):
                area = types.Real.from_mcnp(area)

        if area is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, area)

        self._area: types.Real = area
