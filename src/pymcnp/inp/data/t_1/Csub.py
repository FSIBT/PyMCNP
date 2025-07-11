import re

from . import _option
from ....utils import types
from ....utils import errors


class Csub(_option.TOption_1):
    """
    Represents INP csub elements.

    Attributes:
        count: Number of subdivisions to use.
    """

    _KEYWORD = 'csub'

    _ATTRS = {
        'count': types.Integer,
    }

    _REGEX = re.compile(rf'\Acsub( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, count: str | int | types.Integer):
        """
        Initializes ``Csub``.

        Parameters:
            count: Number of subdivisions to use.

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
            count: Number of subdivisions to use.

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

        if count is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, count)

        self._count: types.Integer = count
