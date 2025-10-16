import re

from . import _option
from ... import types
from ... import errors


class Refpnt(_option.BfldOption):
    """
    Represents INP `refpnt` elements.
    """

    _KEYWORD = 'refpnt'

    _ATTRS = {
        'point': types.Tuple(types.Real),
    }

    _REGEX = re.compile(rf'\Arefpnt((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)

    def __init__(self, point: list[str] | list[float] | list[types.Real]):
        """
        Initializes `Refpnt`.

        Parameters:
            point: Point anywhere on the quadrapole beam.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.point: types.Tuple(types.Real) = point

    @property
    def point(self) -> types.Tuple(types.Real):
        """
        Point anywhere on the quadrapole beam

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
            point: Point anywhere on the quadrapole beam.

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
