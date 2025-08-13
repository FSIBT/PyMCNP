import re

from . import _option
from ... import types
from ... import errors


class Elib(_option.MOption_0):
    """
    Represents INP `elib` elements.
    """

    _KEYWORD = 'elib'

    _ATTRS = {
        'abx': types.String,
    }

    _REGEX = re.compile(rf'\Aelib( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, abx: str | types.String):
        """
        Initializes `Elib`.

        Parameters:
            abx: Default electron table identifier.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.abx: types.String = abx

    @property
    def abx(self) -> types.String:
        """
        Default electron table identifier

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
            abx: Default electron table identifier.

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
