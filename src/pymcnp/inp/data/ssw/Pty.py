import re
import typing
import dataclasses


from ._option import SswOption
from ....utils import types
from ....utils import errors


class Pty(SswOption):
    """
    Represents INP pty elements.

    Attributes:
        tracks: Tracks to record.
    """

    _ATTRS = {
        'tracks': types.Tuple[types.Designator],
    }

    _REGEX = re.compile(rf'\Apty((?: {types.Designator._REGEX.pattern})+?)\Z')

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
class PtyBuilder:
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

        tracks = []
        for item in self.tracks:
            if isinstance(item, types.Designator):
                tracks.append(item)
            elif isinstance(item, str):
                tracks.append(types.Designator.from_mcnp(item))
            else:
                tracks.append(item.build())
        tracks = types.Tuple(tracks)

        return Pty(
            tracks=tracks,
        )
