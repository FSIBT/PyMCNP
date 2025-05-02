import re
import typing
import dataclasses


from . import stop
from ._option import DataOption
from ...utils import types


class Stop(DataOption):
    """
    Represents INP stop elements.

    Attributes:
        options: Dictionary of options.
    """

    _ATTRS = {
        'options': types.Tuple[stop.StopOption],
    }

    _REGEX = re.compile(rf'\Astop((?: (?:{stop.StopOption._REGEX.pattern}))+?)?\Z')

    def __init__(self, options: types.Tuple[stop.StopOption] = None):
        """
        Initializes ``Stop``.

        Parameters:
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                options,
            ]
        )

        self.options: typing.Final[types.Tuple[stop.StopOption]] = options


@dataclasses.dataclass
class StopBuilder:
    """
    Builds ``Stop``.

    Attributes:
        options: Dictionary of options.
    """

    options: list[str] | list[stop.StopOption] = None

    def build(self):
        """
        Builds ``StopBuilder`` into ``Stop``.

        Returns:
            ``Stop`` for ``StopBuilder``.
        """

        options = []
        for item in self.options:
            if isinstance(item, stop.StopOption):
                options.append(item)
            elif isinstance(item, str):
                options.append(stop.StopOption.from_mcnp(item))
            else:
                options.append(item.build())
        options = types.Tuple(options)

        return Stop(
            options=options,
        )
