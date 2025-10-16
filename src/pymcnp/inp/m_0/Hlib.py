import re

from . import _option
from ... import types
from ... import errors


class Hlib(_option.MOption_0):
    """
    Represents INP `hlib` elements.
    """

    _KEYWORD = 'hlib'

    _ATTRS = {
        'abx': types.String,
    }

    _REGEX = re.compile(rf'\Ahlib( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, abx: str | types.String):
        """
        Initializes `Hlib`.

        Parameters:
            abx: Default proton table identifier.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.abx: types.String = abx

    @property
    def abx(self) -> types.String:
        """
        Default proton table identifier

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._abx

    @abx.setter
    def abx(self, abx: str | types.String) -> None:
        """
        Sets `abx`.

        Parameters:
            abx: Default proton table identifier.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if abx is not None:
            if isinstance(abx, types.String):
                abx = abx
            elif isinstance(abx, str):
                abx = types.String.from_mcnp(abx)

        if abx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, abx)

        self._abx: types.String = abx
