import re

from . import _option
from ... import types
from ... import errors


class Pty(_option.SswOption):
    """
    Represents INP `pty` elements.
    """

    _KEYWORD = 'pty'

    _ATTRS = {
        'tracks': types.Tuple(types.Designator),
    }

    _REGEX = re.compile(rf'\Apty((?: {types.Designator._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)

    def __init__(self, tracks: list[str] | list[types.Designator]):
        """
        Initializes `Pty`.

        Parameters:
            tracks: Tracks to record.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.tracks: types.Tuple(types.Designator) = tracks

    @property
    def tracks(self) -> types.Tuple(types.Designator):
        """
        Tracks to record

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._tracks

    @tracks.setter
    def tracks(self, tracks: list[str] | list[types.Designator]) -> None:
        """
        Sets `tracks`.

        Parameters:
            tracks: Tracks to record.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if tracks is not None:
            array = []
            for item in tracks:
                if isinstance(item, types.Designator):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(types.Designator.from_mcnp(item))
            tracks = types.Tuple(types.Designator)(array)

        if tracks is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, tracks)

        self._tracks: types.Tuple(types.Designator) = tracks
