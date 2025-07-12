import re

from . import _option
from ....utils import types
from ....utils import errors


class Par(_option.SdefOption):
    """
    Represents INP par elements.
    """

    _KEYWORD = 'par'

    _ATTRS = {
        'kind': types.String,
    }

    _REGEX = re.compile(rf'\Apar( {types.String._REGEX.pattern[2:-2]})\Z')

    def __init__(self, kind: str | types.String):
        """
        Initializes ``Par``.

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
        Sets ``kind``.

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
