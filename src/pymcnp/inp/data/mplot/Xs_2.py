import re

from . import _option
from ....utils import types
from ....utils import errors


class Xs_2(_option.MplotOption):
    """
    Represents INP xs variation #2 elements.

    Attributes:
        m: Material question mark.
    """

    _KEYWORD = 'xs'

    _ATTRS = {
        'm': types.String,
    }

    _REGEX = re.compile(rf'\Axs( {types.String._REGEX.pattern[2:-2]})\Z')

    def __init__(self, m: str | types.String):
        """
        Initializes ``Xs_2``.

        Parameters:
            m: Material question mark.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.m: types.String = m

    @property
    def m(self) -> types.String:
        """
        Gets ``m``.

        Returns:
            ``m``.
        """

        return self._m

    @m.setter
    def m(self, m: str | types.String) -> None:
        """
        Sets ``m``.

        Parameters:
            m: Material question mark.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if m is not None:
            if isinstance(m, types.String):
                m = m
            elif isinstance(m, str):
                m = types.String.from_mcnp(m)
            else:
                raise TypeError

        if m is None or not (m == '?'):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, m)

        self._m: types.String = m
