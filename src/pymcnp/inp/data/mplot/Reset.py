import re

from . import _option
from ....utils import types
from ....utils import errors


class Reset(_option.MplotOption):
    """
    Represents INP reset elements.

    Attributes:
        aa: Command parameter reset.
    """

    _KEYWORD = 'reset'

    _ATTRS = {
        'aa': types.String,
    }

    _REGEX = re.compile(r'\Areset(?: (all|coplot))?\Z')

    def __init__(self, aa: str | types.String = None):
        """
        Initializes ``Reset``.

        Parameters:
            aa: Command parameter reset.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.aa: types.String = aa

    @property
    def aa(self) -> types.String:
        """
        Gets ``aa``.

        Returns:
            ``aa``.
        """

        return self._aa

    @aa.setter
    def aa(self, aa: str | types.String) -> None:
        """
        Sets ``aa``.

        Parameters:
            aa: Command parameter reset.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if aa is not None:
            if isinstance(aa, types.String):
                aa = aa
            elif isinstance(aa, str):
                aa = types.String.from_mcnp(aa)
            else:
                raise TypeError

        if aa is not None and aa not in {'all', 'coplot'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, aa)

        self._aa: types.String = aa
