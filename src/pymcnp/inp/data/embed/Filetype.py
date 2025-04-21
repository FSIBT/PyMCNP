import re
import typing
import dataclasses


from ._option import EmbedOption
from ....utils import types
from ....utils import errors


class Filetype(EmbedOption, keyword='filetype'):
    """
    Represents INP filetype elements.

    Attributes:
        kind: File type for the elemental edit output file.
    """

    _ATTRS = {
        'kind': types.String,
    }

    _REGEX = re.compile(rf'\Afiletype( {types.String._REGEX.pattern})\Z')

    def __init__(self, kind: types.String):
        """
        Initializes ``Filetype``.

        Parameters:
            kind: File type for the elemental edit output file.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if kind is None or type not in {'ascii', 'binary'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, kind)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                kind,
            ]
        )

        self.kind: typing.Final[types.String] = kind


@dataclasses.dataclass
class FiletypeBuilder:
    """
    Builds ``Filetype``.

    Attributes:
        kind: File type for the elemental edit output file.
    """

    kind: str | types.String

    def build(self):
        """
        Builds ``FiletypeBuilder`` into ``Filetype``.

        Returns:
            ``Filetype`` for ``FiletypeBuilder``.
        """

        if isinstance(self.kind, types.String):
            kind = self.kind
        elif isinstance(self.kind, str):
            kind = types.String.from_mcnp(self.kind)

        return Filetype(
            kind=kind,
        )
