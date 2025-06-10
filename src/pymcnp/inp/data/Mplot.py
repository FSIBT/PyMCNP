import re
import copy
import typing
import dataclasses


from . import mplot
from . import _option
from ...utils import types


class Mplot(_option.DataOption):
    """
    Represents INP mplot elements.

    Attributes:
        options: Dictionary of options.
    """

    _KEYWORD = 'mplot'

    _ATTRS = {
        'options': types.Tuple[mplot.MplotOption],
    }

    _REGEX = re.compile(rf'\Amplot((?: (?:{mplot.MplotOption._REGEX.pattern[2:-2]}))+?)?\Z')

    def __init__(self, options: types.Tuple[mplot.MplotOption] = None):
        """
        Initializes ``Mplot``.

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

        self.options: typing.Final[types.Tuple[mplot.MplotOption]] = options


@dataclasses.dataclass
class MplotBuilder(_option.DataOptionBuilder):
    """
    Builds ``Mplot``.

    Attributes:
        options: Dictionary of options.
    """

    options: list[str] | list[mplot.MplotOption] = None

    def build(self):
        """
        Builds ``MplotBuilder`` into ``Mplot``.

        Returns:
            ``Mplot`` for ``MplotBuilder``.
        """

        if self.options:
            options = []
            for item in self.options:
                if isinstance(item, mplot.MplotOption):
                    options.append(item)
                elif isinstance(item, str):
                    options.append(mplot.MplotOption.from_mcnp(item))
                elif isinstance(item, mplot.MplotOptionBuilder):
                    options.append(item.build())
            options = types.Tuple(options)
        else:
            options = None

        return Mplot(
            options=options,
        )

    @staticmethod
    def unbuild(ast: Mplot):
        """
        Unbuilds ``Mplot`` into ``MplotBuilder``

        Returns:
            ``MplotBuilder`` for ``Mplot``.
        """

        return MplotBuilder(
            options=copy.deepcopy(ast.options),
        )
