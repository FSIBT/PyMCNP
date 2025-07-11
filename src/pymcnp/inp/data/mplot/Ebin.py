import re

from . import _option
from ....utils import types
from ....utils import errors


class Ebin(_option.MplotOption):
    """
    Represents INP ebin elements.

    Attributes:
        n: Energy bin to plot.
    """

    _KEYWORD = 'ebin'

    _ATTRS = {
        'n': types.Integer,
    }

    _REGEX = re.compile(rf'\Aebin( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, n: str | int | types.Integer):
        """
        Initializes ``Ebin``.

        Parameters:
            n: Energy bin to plot.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.n: types.Integer = n

    @property
    def n(self) -> types.Integer:
        """
        Gets ``n``.

        Returns:
            ``n``.
        """

        return self._n

    @n.setter
    def n(self, n: str | int | types.Integer) -> None:
        """
        Sets ``n``.

        Parameters:
            n: Energy bin to plot.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if n is not None:
            if isinstance(n, types.Integer):
                n = n
            elif isinstance(n, int):
                n = types.Integer(n)
            elif isinstance(n, str):
                n = types.Integer.from_mcnp(n)
            else:
                raise TypeError

        if n is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, n)

        self._n: types.Integer = n
