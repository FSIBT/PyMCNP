import re
import copy
import typing
import dataclasses


from . import stop
from . import _option
from ...utils import types


class Stop(_option.DataOption):
    """
    Represents INP stop elements.

    Attributes:
        options: Dictionary of options.
    """

    _KEYWORD = 'stop'

    _ATTRS = {
        'options': types.Tuple[stop.StopOption],
    }

    _REGEX = re.compile(rf'\Astop((?: (?:{stop.StopOption._REGEX.pattern[2:-2]}))+?)?\Z')

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
class StopBuilder(_option.DataOptionBuilder):
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

        if self.options:
            options = []
            for item in self.options:
                if isinstance(item, stop.StopOption):
                    options.append(item)
                elif isinstance(item, str):
                    options.append(stop.StopOption.from_mcnp(item))
                elif isinstance(item, stop.StopOptionBuilder):
                    options.append(item.build())
            options = types.Tuple(options)
        else:
            options = None

        return Stop(
            options=options,
        )

    @staticmethod
    def unbuild(ast: Stop):
        """
        Unbuilds ``Stop`` into ``StopBuilder``

        Returns:
            ``StopBuilder`` for ``Stop``.
        """

        return StopBuilder(
            options=copy.deepcopy(ast.options),
        )
