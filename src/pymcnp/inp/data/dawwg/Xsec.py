import re

from . import _option
from ....utils import types
from ....utils import errors


class Xsec(_option.DawwgOption):
    """
    Represents INP xsec elements.
    """

    _KEYWORD = 'xsec'

    _ATTRS = {
        'count': types.Integer,
    }

    _REGEX = re.compile(rf'\Axsec( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, count: str | int | types.Integer):
        """
        Initializes ``Xsec``.

        Parameters:
            count: Number of sample points for each direction in each mesh.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.count: types.Integer = count

    @property
    def count(self) -> types.Integer:
        """
        Number of sample points for each direction in each mesh

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._count

    @count.setter
    def count(self, count: str | int | types.Integer) -> None:
        """
        Sets ``count``.

        Parameters:
            count: Number of sample points for each direction in each mesh.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if count is not None:
            if isinstance(count, types.Integer):
                count = count
            elif isinstance(count, int):
                count = types.Integer(count)
            elif isinstance(count, str):
                count = types.Integer.from_mcnp(count)

        if count is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, count)

        self._count: types.Integer = count
