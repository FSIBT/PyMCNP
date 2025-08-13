import re

from . import _option
from ... import types
from ... import errors


class Ara_0(_option.SdefOption):
    """
    Represents INP `ara` elements variation #0.
    """

    _KEYWORD = 'ara'

    _ATTRS = {
        'area': types.Real,
    }

    _REGEX = re.compile(rf'\Aara( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, area: str | int | float | types.Real):
        """
        Initializes `Ara_0`.

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
        Sets `area`.

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
