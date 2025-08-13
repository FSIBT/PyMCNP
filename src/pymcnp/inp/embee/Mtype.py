import re

from . import _option
from ... import types
from ... import errors


class Mtype(_option.EmbeeOption):
    """
    Represents INP `mtype` elements.
    """

    _KEYWORD = 'mtype'

    _ATTRS = {
        'kind': types.String,
    }

    _REGEX = re.compile(rf'\Amtype( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, kind: str | types.String):
        """
        Initializes `Mtype`.

        Parameters:
            kind: Multiplier type.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.kind: types.String = kind

    @property
    def kind(self) -> types.String:
        """
        Multiplier type

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._kind

    @kind.setter
    def kind(self, kind: str | types.String) -> None:
        """
        Sets `kind`.

        Parameters:
            kind: Multiplier type.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if kind is not None:
            if isinstance(kind, types.String):
                kind = kind
            elif isinstance(kind, str):
                kind = types.String.from_mcnp(kind)

        if kind is None or kind.value.lower() not in {'flux', 'isotropic', 'population', 'reaction', 'source', 'track'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, kind)

        self._kind: types.String = kind
