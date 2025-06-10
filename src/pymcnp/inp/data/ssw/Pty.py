import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Pty(_option.SswOption):
    """
    Represents INP pty elements.

    Attributes:
        tracks: Tracks to record.
    """

    _KEYWORD = 'pty'

    _ATTRS = {
        'tracks': types.Tuple[types.Designator],
    }

    _REGEX = re.compile(rf'\Apty((?: {types.Designator._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, tracks: types.Tuple[types.Designator]):
        """
        Initializes ``Pty``.

        Parameters:
            tracks: Tracks to record.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if tracks is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, tracks)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                tracks,
            ]
        )

        self.tracks: typing.Final[types.Tuple[types.Designator]] = tracks


@dataclasses.dataclass
class PtyBuilder(_option.SswOptionBuilder):
    """
    Builds ``Pty``.

    Attributes:
        tracks: Tracks to record.
    """

    tracks: list[str] | list[types.Designator]

    def build(self):
        """
        Builds ``PtyBuilder`` into ``Pty``.

        Returns:
            ``Pty`` for ``PtyBuilder``.
        """

        if self.tracks:
            tracks = []
            for item in self.tracks:
                if isinstance(item, types.Designator):
                    tracks.append(item)
                elif isinstance(item, str):
                    tracks.append(types.Designator.from_mcnp(item))
            tracks = types.Tuple(tracks)
        else:
            tracks = None

        return Pty(
            tracks=tracks,
        )

    @staticmethod
    def unbuild(ast: Pty):
        """
        Unbuilds ``Pty`` into ``PtyBuilder``

        Returns:
            ``PtyBuilder`` for ``Pty``.
        """

        return PtyBuilder(
            tracks=copy.deepcopy(ast.tracks),
        )
