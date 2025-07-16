import re

from . import _option
from ... import types
from ... import errors


class Otfdb(_option.DataOption):
    """
    Represents INP otfdb elements.
    """

    _KEYWORD = 'otfdb'

    _ATTRS = {
        'zaids': types.Tuple[types.Zaid],
    }

    _REGEX = re.compile(rf'\Aotfdb((?: {types.Zaid._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, zaids: list[str] | list[types.Zaid]):
        """
        Initializes ``Otfdb``.

        Parameters:
            zaids: Identifiers for the broadening tables.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.zaids: types.Tuple[types.Zaid] = zaids

    @property
    def zaids(self) -> types.Tuple[types.Zaid]:
        """
        Identifiers for the broadening tables

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._zaids

    @zaids.setter
    def zaids(self, zaids: list[str] | list[types.Zaid]) -> None:
        """
        Sets ``zaids``.

        Parameters:
            zaids: Identifiers for the broadening tables.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if zaids is not None:
            array = []
            for item in zaids:
                if isinstance(item, types.Zaid):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(types.Zaid.from_mcnp(item))
            zaids = types.Tuple(array)

        if zaids is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, zaids)

        self._zaids: types.Tuple[types.Zaid] = zaids
