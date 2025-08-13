import re

from . import _option
from ... import types
from ... import errors


class Kints(_option.FmeshOption):
    """
    Represents INP `kints` elements.
    """

    _KEYWORD = 'kints'

    _ATTRS = {
        'count': types.Tuple(types.Integer),
    }

    _REGEX = re.compile(rf'\Akints((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)

    def __init__(self, count: list[str] | list[int] | list[types.Integer]):
        """
        Initializes `Kints`.

        Parameters:
            count: Number of mesh points z/theta for rectangular/cylindrical geometry.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.count: types.Tuple(types.Integer) = count

    @property
    def count(self) -> types.Tuple(types.Integer):
        """
        Number of mesh points z/theta for rectangular/cylindrical geometry

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._count

    @count.setter
    def count(self, count: list[str] | list[int] | list[types.Integer]) -> None:
        """
        Sets `count`.

        Parameters:
            count: Number of mesh points z/theta for rectangular/cylindrical geometry.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if count is not None:
            array = []
            for item in count:
                if isinstance(item, types.Integer):
                    array.append(item)
                elif isinstance(item, int):
                    array.append(types.Integer(item))
                elif isinstance(item, str):
                    array.append(types.Integer.from_mcnp(item))
            count = types.Tuple(types.Integer)(array)

        if count is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, count)

        self._count: types.Tuple(types.Integer) = count
