import re

from . import _option
from ...utils import types
from ...utils import errors


class Dm(_option.DataOption):
    """
    Represents INP dm elements.
    """

    _KEYWORD = 'dm'

    _ATTRS = {
        'suffix': types.Integer,
        'zaids': types.Tuple[types.Zaid],
    }

    _REGEX = re.compile(rf'\Adm(\d+)((?: {types.Zaid._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, suffix: str | int | types.Integer, zaids: list[str] | list[types.Zaid]):
        """
        Initializes ``Dm``.

        Parameters:
            suffix: Data card option suffix.
            zaids: Tuple of ZAID aliases.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.suffix: types.Integer = suffix
        self.zaids: types.Tuple[types.Zaid] = zaids

    @property
    def suffix(self) -> types.Integer:
        """
        Data card option suffix

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._suffix

    @suffix.setter
    def suffix(self, suffix: str | int | types.Integer) -> None:
        """
        Sets ``suffix``.

        Parameters:
            suffix: Data card option suffix.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if suffix is not None:
            if isinstance(suffix, types.Integer):
                suffix = suffix
            elif isinstance(suffix, int):
                suffix = types.Integer(suffix)
            elif isinstance(suffix, str):
                suffix = types.Integer.from_mcnp(suffix)

        if suffix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)

        self._suffix: types.Integer = suffix

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

        if zaids is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, zaids)

        self._zaids: types.Tuple[types.Zaid] = zaids
