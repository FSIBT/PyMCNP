import re
import copy
import typing
import dataclasses


from . import kopts
from . import _option
from ...utils import types


class Kopts(_option.DataOption):
    """
    Represents INP kopts elements.

    Attributes:
        options: Dictionary of options.
    """

    _KEYWORD = 'kopts'

    _ATTRS = {
        'options': types.Tuple[kopts.KoptsOption],
    }

    _REGEX = re.compile(rf'\Akopts((?: (?:{kopts.KoptsOption._REGEX.pattern[2:-2]}))+?)?\Z')

    def __init__(self, options: types.Tuple[kopts.KoptsOption] = None):
        """
        Initializes ``Kopts``.

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

        self.options: typing.Final[types.Tuple[kopts.KoptsOption]] = options


@dataclasses.dataclass
class KoptsBuilder(_option.DataOptionBuilder):
    """
    Builds ``Kopts``.

    Attributes:
        options: Dictionary of options.
    """

    options: list[str] | list[kopts.KoptsOption] = None

    def build(self):
        """
        Builds ``KoptsBuilder`` into ``Kopts``.

        Returns:
            ``Kopts`` for ``KoptsBuilder``.
        """

        if self.options:
            options = []
            for item in self.options:
                if isinstance(item, kopts.KoptsOption):
                    options.append(item)
                elif isinstance(item, str):
                    options.append(kopts.KoptsOption.from_mcnp(item))
                elif isinstance(item, kopts.KoptsOptionBuilder):
                    options.append(item.build())
            options = types.Tuple(options)
        else:
            options = None

        return Kopts(
            options=options,
        )

    @staticmethod
    def unbuild(ast: Kopts):
        """
        Unbuilds ``Kopts`` into ``KoptsBuilder``

        Returns:
            ``KoptsBuilder`` for ``Kopts``.
        """

        return KoptsBuilder(
            options=copy.deepcopy(ast.options),
        )
