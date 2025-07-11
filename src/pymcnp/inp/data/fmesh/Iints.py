import re

from . import _option
from ....utils import types
from ....utils import errors


class Iints(_option.FmeshOption):
    """
    Represents INP iints elements.

    Attributes:
        count: Number of mesh points x/r for rectangular/cylindrical geometry.
    """

    _KEYWORD = 'iints'

    _ATTRS = {
        'count': types.Tuple[types.Integer],
    }

    _REGEX = re.compile(rf'\Aiints((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, count: list[str] | list[int] | list[types.Integer]):
        """
        Initializes ``Iints``.

        Parameters:
            count: Number of mesh points x/r for rectangular/cylindrical geometry.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.count: types.Tuple[types.Integer] = count

    @property
    def count(self) -> types.Tuple[types.Integer]:
        """
        Gets ``count``.

        Returns:
            ``count``.
        """

        return self._count

    @count.setter
    def count(self, count: list[str] | list[int] | list[types.Integer]) -> None:
        """
        Sets ``count``.

        Parameters:
            count: Number of mesh points x/r for rectangular/cylindrical geometry.

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
                else:
                    raise TypeError
            count = types.Tuple(array)

        if count is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, count)

        self._count: types.Tuple[types.Integer] = count
