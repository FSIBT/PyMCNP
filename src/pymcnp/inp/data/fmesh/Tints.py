import re

from . import _option
from .... import types
from .... import errors


class Tints(_option.FmeshOption):
    """
    Represents INP tints elements.
    """

    _KEYWORD = 'tints'

    _ATTRS = {
        'count': types.Integer,
    }

    _REGEX = re.compile(rf'\Atints( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, count: str | int | types.Integer):
        """
        Initializes ``Tints``.

        Parameters:
            count: Number of mesh points for each mesh time.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.count: types.Integer = count

    @property
    def count(self) -> types.Integer:
        """
        Number of mesh points for each mesh time

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
            count: Number of mesh points for each mesh time.

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
