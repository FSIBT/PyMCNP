import re
import typing
import dataclasses


from . import mplot
from ._option import DataOption
from ...utils import types


class Mplot(DataOption):
    """
    Represents INP mplot elements.

    Attributes:
        options: Dictionary of options.
    """

    _ATTRS = {
        'options': types.Tuple[mplot.MplotOption],
    }

    _REGEX = re.compile(rf'\Amplot((?: (?:{mplot.MplotOption._REGEX.pattern}))+?)?\Z')

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
class MplotBuilder:
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
                else:
                    options.append(item.build())
            options = types.Tuple(options)
        else:
            options = None

        return Mplot(
            options=options,
        )
