import re
import typing
import dataclasses


from .option_ import SdefOption_
from ....utils import types
from ....utils import errors


class Par(SdefOption_, keyword='par'):
    """
    Represents INP par elements.

    Attributes:
        kind: Source particle type.
    """

    _ATTRS = {
        'kind': types.String,
    }

    _REGEX = re.compile(rf'\Apar( {types.String._REGEX.pattern})\Z')

    def __init__(self, kind: types.String):
        """
        Initializes ``Par``.

        Parameters:
            kind: Source particle type.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if kind is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, kind)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                kind,
            ]
        )

        self.kind: typing.Final[types.String] = kind


@dataclasses.dataclass
class ParBuilder:
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

        if isinstance(self.kind, types.String):
            kind = self.kind
        elif isinstance(self.kind, str):
            kind = types.String.from_mcnp(self.kind)

        return Par(
            kind=kind,
        )
