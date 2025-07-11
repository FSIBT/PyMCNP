import re

from . import _option
from ....utils import types
from ....utils import errors


class Slib(_option.MOption_0):
    """
    Represents INP slib elements.

    Attributes:
        abx: Default helion table identifier.
    """

    _KEYWORD = 'slib'

    _ATTRS = {
        'abx': types.String,
    }

    _REGEX = re.compile(rf'\Aslib( {types.String._REGEX.pattern[2:-2]})\Z')

    def __init__(self, abx: str | types.String):
        """
        Initializes ``Slib``.

        Parameters:
            abx: Default helion table identifier.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.abx: types.String = abx

    @property
    def abx(self) -> types.String:
        """
        Gets ``abx``.

        Returns:
            ``abx``.
        """

        return self._abx

    @abx.setter
    def abx(self, abx: str | types.String) -> None:
        """
        Sets ``abx``.

        Parameters:
            abx: Default helion table identifier.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if abx is not None:
            if isinstance(abx, types.String):
                abx = abx
            elif isinstance(abx, str):
                abx = types.String.from_mcnp(abx)
            else:
                raise TypeError

        if abx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, abx)

        self._abx: types.String = abx
