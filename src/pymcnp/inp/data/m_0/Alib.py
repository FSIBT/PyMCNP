import re

from . import _option
from ....utils import types
from ....utils import errors


class Alib(_option.MOption_0):
    """
    Represents INP alib elements.

    Attributes:
        abx: Default alpha table identifier.
    """

    _KEYWORD = 'alib'

    _ATTRS = {
        'abx': types.String,
    }

    _REGEX = re.compile(rf'\Aalib( {types.String._REGEX.pattern[2:-2]})\Z')

    def __init__(self, abx: str | types.String):
        """
        Initializes ``Alib``.

        Parameters:
            abx: Default alpha table identifier.

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
            abx: Default alpha table identifier.

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
