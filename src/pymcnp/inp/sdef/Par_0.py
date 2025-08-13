import re

from . import _option
from ... import types
from ... import errors


class Par_0(_option.SdefOption):
    """
    Represents INP `par` elements variation #0.
    """

    _KEYWORD = 'par'

    _ATTRS = {
        'kind': types.String,
    }

    _REGEX = re.compile(rf'\Apar( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, kind: str | types.String):
        """
        Initializes `Par_0`.

        Parameters:
            kind: Source particle type.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.kind: types.String = kind

    @property
    def kind(self) -> types.String:
        """
        Source particle type

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
            kind: Source particle type.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if kind is not None:
            if isinstance(kind, types.String):
                kind = kind
            elif isinstance(kind, str):
                kind = types.String.from_mcnp(kind)

        if kind is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, kind)

        self._kind: types.String = kind
