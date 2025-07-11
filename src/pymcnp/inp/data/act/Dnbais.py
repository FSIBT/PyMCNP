import re

from . import _option
from ....utils import types
from ....utils import errors


class Dnbais(_option.ActOption):
    """
    Represents INP dnbais elements.

    Attributes:
        count: Maximum number of neutrons generated per reaction.
    """

    _KEYWORD = 'dnbais'

    _ATTRS = {
        'count': types.Integer,
    }

    _REGEX = re.compile(rf'\Adnbais( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, count: str | int | types.Integer):
        """
        Initializes ``Dnbais``.

        Parameters:
            count: Maximum number of neutrons generated per reaction.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.count: types.Integer = count

    @property
    def count(self) -> types.Integer:
        """
        Gets ``count``.

        Returns:
            ``count``.
        """

        return self._count

    @count.setter
    def count(self, count: str | int | types.Integer) -> None:
        """
        Sets ``count``.

        Parameters:
            count: Maximum number of neutrons generated per reaction.

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
            else:
                raise TypeError

        if count is None or not (count >= 0 and count <= 10):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, count)

        self._count: types.Integer = count
