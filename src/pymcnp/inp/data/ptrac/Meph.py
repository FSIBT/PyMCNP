import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Meph(_option.PtracOption):
    """
    Represents INP meph elements.

    Attributes:
        events: Maximum number of events per history to write.
    """

    _KEYWORD = 'meph'

    _ATTRS = {
        'events': types.Integer,
    }

    _REGEX = re.compile(rf'\Ameph( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, events: types.Integer):
        """
        Initializes ``Meph``.

        Parameters:
            events: Maximum number of events per history to write.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if events is None or not (events > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, events)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                events,
            ]
        )

        self.events: typing.Final[types.Integer] = events


@dataclasses.dataclass
class MephBuilder(_option.PtracOptionBuilder):
    """
    Builds ``Meph``.

    Attributes:
        events: Maximum number of events per history to write.
    """

    events: str | int | types.Integer

    def build(self):
        """
        Builds ``MephBuilder`` into ``Meph``.

        Returns:
            ``Meph`` for ``MephBuilder``.
        """

        events = self.events
        if isinstance(self.events, types.Integer):
            events = self.events
        elif isinstance(self.events, int):
            events = types.Integer(self.events)
        elif isinstance(self.events, str):
            events = types.Integer.from_mcnp(self.events)

        return Meph(
            events=events,
        )

    @staticmethod
    def unbuild(ast: Meph):
        """
        Unbuilds ``Meph`` into ``MephBuilder``

        Returns:
            ``MephBuilder`` for ``Meph``.
        """

        return MephBuilder(
            events=copy.deepcopy(ast.events),
        )
