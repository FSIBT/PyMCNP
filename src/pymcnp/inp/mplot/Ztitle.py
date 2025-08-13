import re

from . import _option
from ... import types
from ... import errors


class Ztitle(_option.MplotOption):
    """
    Represents INP `ztitle` elements.
    """

    _KEYWORD = 'ztitle'

    _ATTRS = {
        'aa': types.String,
    }

    _REGEX = re.compile(rf'\Aztitle( \"{types.String._REGEX.pattern[2:-2]}\")\Z', re.IGNORECASE)

    def __init__(self, aa: str | types.String):
        """
        Initializes `Ztitle`.

        Parameters:
            aa: Line to substitute.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.aa: types.String = aa

    @property
    def aa(self) -> types.String:
        """
        Line to substitute

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
            aa: Line to substitute.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if aa is not None:
            if isinstance(aa, types.String):
                aa = aa
            elif isinstance(aa, str):
                aa = types.String.from_mcnp(aa)

        if aa is None or not (len(aa) <= 40):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, aa)

        self._aa: types.String = aa
