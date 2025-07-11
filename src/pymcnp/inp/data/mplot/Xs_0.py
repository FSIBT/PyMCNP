import re

from . import _option
from ....utils import types
from ....utils import errors


class Xs_0(_option.MplotOption):
    """
    Represents INP xs variation #0 elements.

    Attributes:
        m: Material number.
    """

    _KEYWORD = 'xs'

    _ATTRS = {
        'm': types.Integer,
    }

    _REGEX = re.compile(rf'\Axs( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, m: str | int | types.Integer):
        """
        Initializes ``Xs_0``.

        Parameters:
            m: Material number.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.m: types.Integer = m

    @property
    def m(self) -> types.Integer:
        """
        Gets ``m``.

        Returns:
            ``m``.
        """

        return self._m

    @m.setter
    def m(self, m: str | int | types.Integer) -> None:
        """
        Sets ``m``.

        Parameters:
            m: Material number.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if m is not None:
            if isinstance(m, types.Integer):
                m = m
            elif isinstance(m, int):
                m = types.Integer(m)
            elif isinstance(m, str):
                m = types.Integer.from_mcnp(m)
            else:
                raise TypeError

        if m is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, m)

        self._m: types.Integer = m
