import re
import typing


from .option_ import SswOption_
from ....utils import types
from ....utils import errors


class Pty(SswOption_, keyword='pty'):
    """
    Represents INP pty elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
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
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if tracks is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, tracks)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                tracks,
            ]
        )

        self.tracks: typing.Final[types.Tuple[types.Designator]] = tracks
