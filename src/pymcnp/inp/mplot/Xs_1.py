import re

from . import _option
from ... import types
from ... import errors


class Xs_1(_option.MplotOption):
    """
    Represents INP `xs` elements variation #1.
    """

    _KEYWORD = 'xs'

    _ATTRS = {
        'm': types.Zaid,
    }

    _REGEX = re.compile(rf'\Axs( {types.Zaid._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, m: str | types.Zaid):
        """
        Initializes `Xs_1`.

        Parameters:
            m: Material ZAID.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.m: types.Zaid = m

    @property
    def m(self) -> types.Zaid:
        """
        Material ZAID

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._m

    @m.setter
    def m(self, m: str | types.Zaid) -> None:
        """
        Sets `m`.

        Parameters:
            m: Material ZAID.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if m is not None:
            if isinstance(m, types.Zaid):
                m = m
            elif isinstance(m, str):
                m = types.Zaid.from_mcnp(m)

        if m is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, m)

        self._m: types.Zaid = m
