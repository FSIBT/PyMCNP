import re
import copy
import typing
import dataclasses


from . import act
from . import _option
from ...utils import types


class Act(_option.DataOption):
    """
    Represents INP act elements.

    Attributes:
        options: Dictionary of options.
    """

    _KEYWORD = 'act'

    _ATTRS = {
        'options': types.Tuple[act.ActOption],
    }

    _REGEX = re.compile(rf'\Aact((?: (?:{act.ActOption._REGEX.pattern[2:-2]}))+?)?\Z')

    def __init__(self, options: types.Tuple[act.ActOption] = None):
        """
        Initializes ``Act``.

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

        self.options: typing.Final[types.Tuple[act.ActOption]] = options


@dataclasses.dataclass
class ActBuilder(_option.DataOptionBuilder):
    """
    Builds ``Act``.

    Attributes:
        options: Dictionary of options.
    """

    options: list[str] | list[act.ActOption] = None

    def build(self):
        """
        Builds ``ActBuilder`` into ``Act``.

        Returns:
            ``Act`` for ``ActBuilder``.
        """

        if self.options:
            options = []
            for item in self.options:
                if isinstance(item, act.ActOption):
                    options.append(item)
                elif isinstance(item, str):
                    options.append(act.ActOption.from_mcnp(item))
                elif isinstance(item, act.ActOptionBuilder):
                    options.append(item.build())
            options = types.Tuple(options)
        else:
            options = None

        return Act(
            options=options,
        )

    @staticmethod
    def unbuild(ast: Act):
        """
        Unbuilds ``Act`` into ``ActBuilder``

        Returns:
            ``ActBuilder`` for ``Act``.
        """

        return ActBuilder(
            options=copy.deepcopy(ast.options),
        )
