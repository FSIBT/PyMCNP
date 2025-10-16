import re

from . import _option
from ... import types
from ... import errors


class Filetype(_option.EmbedOption):
    """
    Represents INP `filetype` elements.
    """

    _KEYWORD = 'filetype'

    _ATTRS = {
        'kind': types.String,
    }

    _REGEX = re.compile(rf'\Afiletype( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, kind: str | types.String):
        """
        Initializes `Filetype`.

        Parameters:
            kind: File type for the elemental edit output file.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.kind: types.String = kind

    @property
    def kind(self) -> types.String:
        """
        File type for the elemental edit output file

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
            kind: File type for the elemental edit output file.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if kind is not None:
            if isinstance(kind, types.String):
                kind = kind
            elif isinstance(kind, str):
                kind = types.String.from_mcnp(kind)

        if kind is None or kind.value.lower() not in {'ascii', 'binary'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, kind)

        self._kind: types.String = kind
