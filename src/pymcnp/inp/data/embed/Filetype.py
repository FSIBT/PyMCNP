import re
import copy
import typing
import dataclasses


from ._option import EmbedOption
from ....utils import types
from ....utils import errors


class Filetype(EmbedOption):
    """
    Represents INP filetype elements.

    Attributes:
        kind: File type for the elemental edit output file.
    """

    _KEYWORD = 'filetype'

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

        if kind is None or kind not in {'ascii', 'binary'}:
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

        kind = self.kind
        if isinstance(self.kind, types.String):
            kind = self.kind
        elif isinstance(self.kind, str):
            kind = types.String.from_mcnp(self.kind)

        return Filetype(
            kind=kind,
        )

    @staticmethod
    def unbuild(ast: Filetype):
        """
        Unbuilds ``Filetype`` into ``FiletypeBuilder``

        Returns:
            ``FiletypeBuilder`` for ``Filetype``.
        """

        return Filetype(
            kind=copy.deepcopy(ast.kind),
        )
