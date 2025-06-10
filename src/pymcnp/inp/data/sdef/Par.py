import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Par(_option.SdefOption):
    """
    Represents INP par elements.

    Attributes:
        kind: Source particle type.
    """

    _KEYWORD = 'par'

    _ATTRS = {
        'kind': types.String,
    }

    _REGEX = re.compile(rf'\Apar( {types.String._REGEX.pattern[2:-2]})\Z')

    def __init__(self, kind: types.String):
        """
        Initializes ``Par``.

        Parameters:
            kind: Source particle type.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if kind is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, kind)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                kind,
            ]
        )

        self.kind: typing.Final[types.String] = kind


@dataclasses.dataclass
class ParBuilder(_option.SdefOptionBuilder):
    """
    Builds ``Par``.

    Attributes:
        kind: Source particle type.
    """

    kind: str | types.String

    def build(self):
        """
        Builds ``ParBuilder`` into ``Par``.

        Returns:
            ``Par`` for ``ParBuilder``.
        """

        kind = self.kind
        if isinstance(self.kind, types.String):
            kind = self.kind
        elif isinstance(self.kind, str):
            kind = types.String.from_mcnp(self.kind)

        return Par(
            kind=kind,
        )

    @staticmethod
    def unbuild(ast: Par):
        """
        Unbuilds ``Par`` into ``ParBuilder``

        Returns:
            ``ParBuilder`` for ``Par``.
        """

        return ParBuilder(
            kind=copy.deepcopy(ast.kind),
        )
