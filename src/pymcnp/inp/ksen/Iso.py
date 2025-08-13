import re

from . import _option
from ... import types
from ... import errors


class Iso(_option.KsenOption):
    """
    Represents INP `iso` elements.
    """

    _KEYWORD = 'iso'

    _ATTRS = {
        'zaids': types.Tuple(types.Zaid),
    }

    _REGEX = re.compile(rf'\Aiso((?: {types.Zaid._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)

    def __init__(self, zaids: list[str] | list[types.Zaid]):
        """
        Initializes `Iso`.

        Parameters:
            zaids: List of ZAIDs for pertubation.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.zaids: types.Tuple(types.Zaid) = zaids

    @property
    def zaids(self) -> types.Tuple(types.Zaid):
        """
        List of ZAIDs for pertubation

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._zaids

    @zaids.setter
    def zaids(self, zaids: list[str] | list[types.Zaid]) -> None:
        """
        Sets `zaids`.

        Parameters:
            zaids: List of ZAIDs for pertubation.

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
            zaids = types.Tuple(types.Zaid)(array)

        if zaids is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, zaids)

        self._zaids: types.Tuple(types.Zaid) = zaids
