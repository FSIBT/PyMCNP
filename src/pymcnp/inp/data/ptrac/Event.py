import re
import copy
import typing
import dataclasses


from ._option import PtracOption
from ....utils import types
from ....utils import errors


class Event(PtracOption):
    """
    Represents INP event elements.

    Attributes:
        settings: Specifies the type of events written to the PTRAC file.
    """

    _KEYWORD = 'event'

    _ATTRS = {
        'settings': types.Tuple[types.String],
    }

    _REGEX = re.compile(rf'\Aevent((?: {types.String._REGEX.pattern})+?)\Z')

    def __init__(self, settings: types.Tuple[types.String]):
        """
        Initializes ``Event``.

        Parameters:
            settings: Specifies the type of events written to the PTRAC file.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if settings is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, settings)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                settings,
            ]
        )

        self.settings: typing.Final[types.Tuple[types.String]] = settings


@dataclasses.dataclass
class EventBuilder:
    """
    Builds ``Event``.

    Attributes:
        settings: Specifies the type of events written to the PTRAC file.
    """

    settings: list[str] | list[types.String]

    def build(self):
        """
        Builds ``EventBuilder`` into ``Event``.

        Returns:
            ``Event`` for ``EventBuilder``.
        """

        if self.settings:
            settings = []
            for item in self.settings:
                if isinstance(item, types.String):
                    settings.append(item)
                elif isinstance(item, str):
                    settings.append(types.String.from_mcnp(item))
                else:
                    settings.append(item.build())
            settings = types.Tuple(settings)
        else:
            settings = None

        return Event(
            settings=settings,
        )

    @staticmethod
    def unbuild(ast: Event):
        """
        Unbuilds ``Event`` into ``EventBuilder``

        Returns:
            ``EventBuilder`` for ``Event``.
        """

        return Event(
            settings=copy.deepcopy(ast.settings),
        )
