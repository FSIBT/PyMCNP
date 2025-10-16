import re

from . import _option
from ... import types
from ... import errors


class Ref(_option.MeshOption):
    """
    Represents INP `ref` elements.
    """

    _KEYWORD = 'ref'

    _ATTRS = {
        'point': types.Tuple(types.Real),
    }

    _REGEX = re.compile(rf'\Aref((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)

    def __init__(self, point: list[str] | list[float] | list[types.Real]):
        """
        Initializes `Ref`.

        Parameters:
            point: Mesh reference point.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.point: types.Tuple(types.Real) = point

    @property
    def point(self) -> types.Tuple(types.Real):
        """
        Mesh reference point

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._point

    @point.setter
    def point(self, point: list[str] | list[float] | list[types.Real]) -> None:
        """
        Sets `point`.

        Parameters:
            point: Mesh reference point.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if point is not None:
            array = []
            for item in point:
                if isinstance(item, types.Real):
                    array.append(item)
                elif isinstance(item, int) or isinstance(item, float):
                    array.append(types.Real(item))
                elif isinstance(item, str):
                    array.append(types.Real.from_mcnp(item))
            point = types.Tuple(types.Real)(array)

        if point is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, point)

        self._point: types.Tuple(types.Real) = point
