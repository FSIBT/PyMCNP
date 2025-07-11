import re

from . import _option
from ....utils import types
from ....utils import errors


class Fission(_option.ActOption):
    """
    Represents INP fission elements.

    Attributes:
        kind: Type of delayed particle(s) to be produced from residuals created by fission.
    """

    _KEYWORD = 'fission'

    _ATTRS = {
        'kind': types.String,
    }

    _REGEX = re.compile(rf'\Afission( {types.String._REGEX.pattern[2:-2]})\Z')

    def __init__(self, kind: str | types.String):
        """
        Initializes ``Fission``.

        Parameters:
            kind: Type of delayed particle(s) to be produced from residuals created by fission.

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
            kind: Type of delayed particle(s) to be produced from residuals created by fission.

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
