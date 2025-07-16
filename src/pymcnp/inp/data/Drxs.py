import re

from . import _option
from ... import types


class Drxs(_option.DataOption):
    """
    Represents INP drxs elements.
    """

    _KEYWORD = 'drxs'

    _ATTRS = {
        'zaids': types.Tuple[types.Zaid],
    }

    _REGEX = re.compile(rf'\Adrxs((?: {types.Zaid._REGEX.pattern[2:-2]})+?)?\Z')

    def __init__(self, zaids: list[str] | list[types.Zaid] = None):
        """
        Initializes ``Drxs``.

        Parameters:
            zaids: Tuple of ZAID aliases.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.zaids: types.Tuple[types.Zaid] = zaids

    @property
    def zaids(self) -> types.Tuple[types.Zaid]:
        """
        Tuple of ZAID aliases

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
            zaids: Tuple of ZAID aliases.

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

        self._zaids: types.Tuple[types.Zaid] = zaids
