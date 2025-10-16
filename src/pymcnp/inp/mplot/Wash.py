import re

from . import _option
from ... import types
from ... import errors


class Wash(_option.MplotOption):
    """
    Represents INP `wash` elements.
    """

    _KEYWORD = 'wash'

    _ATTRS = {
        'aa': types.String,
    }

    _REGEX = re.compile(rf'\Awash( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, aa: str | types.String):
        """
        Initializes `Wash`.

        Parameters:
            aa: Color-wash on/offs.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.aa: types.String = aa

    @property
    def aa(self) -> types.String:
        """
        Color-wash on/offs

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
            aa: Color-wash on/offs.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if aa is not None:
            if isinstance(aa, types.String):
                aa = aa
            elif isinstance(aa, str):
                aa = types.String.from_mcnp(aa)

        if aa is None or aa.value.lower() not in {'on', 'off'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, aa)

        self._aa: types.String = aa
