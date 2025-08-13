import re

from . import _option
from ... import types
from ... import errors


class Tlib(_option.MOption_0):
    """
    Represents INP `tlib` elements.
    """

    _KEYWORD = 'tlib'

    _ATTRS = {
        'abx': types.String,
    }

    _REGEX = re.compile(rf'\Atlib( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, abx: str | types.String):
        """
        Initializes `Tlib`.

        Parameters:
            abx: Default triton table identifier.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.abx: types.String = abx

    @property
    def abx(self) -> types.String:
        """
        Default triton table identifier

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
            abx: Default triton table identifier.

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
