import re

from . import _option
from ... import types
from ... import errors


class Dg(_option.ActOption):
    """
    Represents INP `dg` elements.
    """

    _KEYWORD = 'dg'

    _ATTRS = {
        'source': types.String,
    }

    _REGEX = re.compile(rf'\Adg( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, source: str | types.String):
        """
        Initializes `Dg`.

        Parameters:
            source: Delayed gamma data source.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.source: types.String = source

    @property
    def source(self) -> types.String:
        """
        Delayed gamma data source

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._source

    @source.setter
    def source(self, source: str | types.String) -> None:
        """
        Sets `source`.

        Parameters:
            source: Delayed gamma data source.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if source is not None:
            if isinstance(source, types.String):
                source = source
            elif isinstance(source, str):
                source = types.String.from_mcnp(source)

        if source is None or source.value.lower() not in {'line', 'mg', 'none'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, source)

        self._source: types.String = source
