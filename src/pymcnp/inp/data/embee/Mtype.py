import re
import typing
import dataclasses


from .option_ import EmbeeOption_
from ....utils import types
from ....utils import errors


class Mtype(EmbeeOption_, keyword='mtype'):
    """
    Represents INP mtype elements.

    Attributes:
        kind: Multiplier type.
    """

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
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if kind is None or type not in {
            'flux',
            'isotropic',
            'population',
            'reaction',
            'source',
            'track',
        }:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, kind)

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

        if isinstance(self.kind, types.String):
            kind = self.kind
        elif isinstance(self.kind, str):
            kind = types.String.from_mcnp(self.kind)

        return Mtype(
            kind=kind,
        )
