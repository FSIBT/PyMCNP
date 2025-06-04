import re
import copy
import typing
import dataclasses


from ._option import ActOption
from ....utils import types
from ....utils import errors


class Nonfiss(ActOption):
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

    def __init__(self, kind: types.String):
        """
        Initializes ``Nonfiss``.

        Parameters:
            kind: Type of delayed particle(s) to be produced by simple multi-particle reaction.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if kind is None or kind not in {'none', 'n,p,e,f,a', 'all'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, kind)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                kind,
            ]
        )

        self.kind: typing.Final[types.String] = kind


@dataclasses.dataclass
class NonfissBuilder:
    """
    Builds ``Nonfiss``.

    Attributes:
        kind: Type of delayed particle(s) to be produced by simple multi-particle reaction.
    """

    kind: str | types.String

    def build(self):
        """
        Builds ``NonfissBuilder`` into ``Nonfiss``.

        Returns:
            ``Nonfiss`` for ``NonfissBuilder``.
        """

        kind = self.kind
        if isinstance(self.kind, types.String):
            kind = self.kind
        elif isinstance(self.kind, str):
            kind = types.String.from_mcnp(self.kind)

        return Nonfiss(
            kind=kind,
        )

    @staticmethod
    def unbuild(ast: Nonfiss):
        """
        Unbuilds ``Nonfiss`` into ``NonfissBuilder``

        Returns:
            ``NonfissBuilder`` for ``Nonfiss``.
        """

        return Nonfiss(
            kind=copy.deepcopy(ast.kind),
        )
