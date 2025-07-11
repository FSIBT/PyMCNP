import re

from . import _option
from ....utils import types
from ....utils import errors


class Iso(_option.KsenOption):
    """
    Represents INP iso elements.

    Attributes:
        zaids: List of ZAIDs for pertubation.
    """

    _KEYWORD = 'iso'

    _ATTRS = {
        'zaids': types.Tuple[types.Zaid],
    }

    _REGEX = re.compile(rf'\Aiso((?: {types.Zaid._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, zaids: list[str] | list[types.Zaid]):
        """
        Initializes ``Iso``.

        Parameters:
            zaids: List of ZAIDs for pertubation.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.zaids: types.Tuple[types.Zaid] = zaids

    @property
    def zaids(self) -> types.Tuple[types.Zaid]:
        """
        Gets ``zaids``.

        Returns:
            ``zaids``.
        """

        return self._zaids

    @zaids.setter
    def zaids(self, zaids: list[str] | list[types.Zaid]) -> None:
        """
        Sets ``zaids``.

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
                else:
                    raise TypeError
            zaids = types.Tuple(array)

        if zaids is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, zaids)

        self._zaids: types.Tuple[types.Zaid] = zaids
