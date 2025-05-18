import re
import typing
import dataclasses


from ._option import ActOption
from ....utils import types
from ....utils import errors


class Fission(ActOption):
    """
    Represents INP fission elements.

    Attributes:
        kind: Type of delayed particle(s) to be produced from residuals created by fission.
    """

    _ATTRS = {
        'kind': types.String,
    }

    _REGEX = re.compile(rf'\Afission( {types.String._REGEX.pattern})\Z')

    def __init__(self, kind: types.String):
        """
        Initializes ``Fission``.

        Parameters:
            kind: Type of delayed particle(s) to be produced from residuals created by fission.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if kind is None or type not in {'none', 'n,p,e,f,a', 'all'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, kind)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                kind,
            ]
        )

        self.kind: typing.Final[types.String] = kind


@dataclasses.dataclass
class FissionBuilder:
    """
    Builds ``Fission``.

    Attributes:
        kind: Type of delayed particle(s) to be produced from residuals created by fission.
    """

    kind: str | types.String

    def build(self):
        """
        Builds ``FissionBuilder`` into ``Fission``.

        Returns:
            ``Fission`` for ``FissionBuilder``.
        """

        kind = self.kind
        if isinstance(self.kind, types.String):
            kind = self.kind
        elif isinstance(self.kind, str):
            kind = types.String.from_mcnp(self.kind)

        return Fission(
            kind=kind,
        )
