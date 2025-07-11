import re

from . import _option
from ....utils import types


class Pert(_option.MplotOption):
    """
    Represents INP pert elements.

    Attributes:
        n: Number on a PERT card.
    """

    _KEYWORD = 'pert'

    _ATTRS = {
        'n': types.Integer,
    }

    _REGEX = re.compile(rf'\Apert( {types.Integer._REGEX.pattern[2:-2]})?\Z')

    def __init__(self, n: str | int | types.Integer = None):
        """
        Initializes ``Pert``.

        Parameters:
            n: Number on a PERT card.

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
            n: Number on a PERT card.

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

        self._n: types.Integer = n
