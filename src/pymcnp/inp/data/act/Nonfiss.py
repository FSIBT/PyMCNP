import re

from . import _option
from ....utils import types
from ....utils import errors


class Nonfiss(_option.ActOption):
    """
    Represents INP nonfiss elements.

    Attributes:
        kind: Type of delayed particle(s) to be produced by simple multi-particle reaction.
    """

    _KEYWORD = 'nonfiss'

    _ATTRS = {
        'kind': types.String,
    }

    _REGEX = re.compile(rf'\Anonfiss( {types.String._REGEX.pattern[2:-2]})\Z')

    def __init__(self, kind: str | types.String):
        """
        Initializes ``Nonfiss``.

        Parameters:
            kind: Type of delayed particle(s) to be produced by simple multi-particle reaction.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.kind: types.String = kind

    @property
    def kind(self) -> types.String:
        """
        Gets ``kind``.

        Returns:
            ``kind``.
        """

        return self._kind

    @kind.setter
    def kind(self, kind: str | types.String) -> None:
        """
        Sets ``kind``.

        Parameters:
            kind: Type of delayed particle(s) to be produced by simple multi-particle reaction.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if kind is not None:
            if isinstance(kind, types.String):
                kind = kind
            elif isinstance(kind, str):
                kind = types.String.from_mcnp(kind)
            else:
                raise TypeError

        if kind is None or kind not in {'none', 'n,p,e,f,a', 'all'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, kind)

        self._kind: types.String = kind
