import re

from . import _option
from ... import types
from ... import errors


class Reset(_option.MplotOption):
    """
    Represents INP `reset` elements.
    """

    _KEYWORD = 'reset'

    _ATTRS = {
        'aa': types.String,
    }

    _REGEX = re.compile(r'\Areset(?: (all|coplot))?\Z', re.IGNORECASE)

    def __init__(self, aa: str | types.String = None):
        """
        Initializes `Reset`.

        Parameters:
            aa: Command parameter reset.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.aa: types.String = aa

    @property
    def aa(self) -> types.String:
        """
        Command parameter reset

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._aa

    @aa.setter
    def aa(self, aa: str | types.String) -> None:
        """
        Sets `aa`.

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

        if aa is not None and aa.value.lower() not in {'all', 'coplot'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, aa)

        self._aa: types.String = aa
