import re
import typing
import dataclasses


from . import kopts
from ._option import DataOption
from ...utils import types


class Kopts(DataOption):
    """
    Represents INP kopts elements.

    Attributes:
        options: Dictionary of options.
    """

    _ATTRS = {
        'options': types.Tuple[kopts.KoptsOption],
    }

    _REGEX = re.compile(rf'\Akopts((?: (?:{kopts.KoptsOption._REGEX.pattern}))+?)?\Z')

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
class KoptsBuilder:
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

        options = []
        for item in self.options:
            if isinstance(item, kopts.KoptsOption):
                options.append(item)
            elif isinstance(item, str):
                options.append(kopts.KoptsOption.from_mcnp(item))
            else:
                options.append(item.build())
        options = types.Tuple(options)

        return Kopts(
            options=options,
        )
