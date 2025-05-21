import re
import copy
import typing
import dataclasses


from ._option import EmbeeOption
from ....utils import types
from ....utils import errors


class Mtype(EmbeeOption):
    """
    Represents INP mtype elements.

    Attributes:
        kind: Multiplier type.
    """

    _KEYWORD = 'mtype'

    _ATTRS = {
        'kind': types.String,
    }

    _REGEX = re.compile(rf'\Amtype( {types.String._REGEX.pattern})\Z')

    def __init__(self, kind: types.String):
        """
        Initializes ``Mtype``.

        Parameters:
            kind: Multiplier type.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if kind is None or kind not in {
            'flux',
            'isotropic',
            'population',
            'reaction',
            'source',
            'track',
        }:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, kind)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                kind,
            ]
        )

        self.kind: typing.Final[types.String] = kind


@dataclasses.dataclass
class MtypeBuilder:
    """
    Builds ``Mtype``.

    Attributes:
        kind: Multiplier type.
    """

    kind: str | types.String

    def build(self):
        """
        Builds ``MtypeBuilder`` into ``Mtype``.

        Returns:
            ``Mtype`` for ``MtypeBuilder``.
        """

        kind = self.kind
        if isinstance(self.kind, types.String):
            kind = self.kind
        elif isinstance(self.kind, str):
            kind = types.String.from_mcnp(self.kind)

        return Mtype(
            kind=kind,
        )

    @staticmethod
    def unbuild(ast: Mtype):
        """
        Unbuilds ``Mtype`` into ``MtypeBuilder``

        Returns:
            ``MtypeBuilder`` for ``Mtype``.
        """

        return Mtype(
            kind=copy.deepcopy(ast.kind),
        )
