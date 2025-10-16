import re

from . import _option
from ... import types
from ... import errors


class Nap(_option.ActOption):
    """
    Represents INP `nap` elements.
    """

    _KEYWORD = 'nap'

    _ATTRS = {
        'count': types.Integer,
    }

    _REGEX = re.compile(rf'\Anap( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, count: str | int | types.Integer):
        """
        Initializes `Nap`.

        Parameters:
            count: Number of activation products.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.count: types.Integer = count

    @property
    def count(self) -> types.Integer:
        """
        Number of activation products

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._count

    @count.setter
    def count(self, count: str | int | types.Integer) -> None:
        """
        Sets `count`.

        Parameters:
            count: Number of activation products.

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

        if count is None or not (count >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, count)

        self._count: types.Integer = count
