import re
import typing
import dataclasses


from . import rand
from ._option import DataOption
from ...utils import types


class Rand(DataOption, keyword='rand'):
    """
    Represents INP rand elements.

    Attributes:
        options: Dictionary of options.
    """

    _ATTRS = {
        'options': types.Tuple[rand.RandOption],
    }

    _REGEX = re.compile(rf'\Arand((?: (?:{rand.RandOption._REGEX.pattern}))+?)?\Z')

    def __init__(self, options: types.Tuple[rand.RandOption] = None):
        """
        Initializes ``Rand``.

        Parameters:
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                options,
            ]
        )

        self.options: typing.Final[types.Tuple[rand.RandOption]] = options


@dataclasses.dataclass
class RandBuilder:
    """
    Builds ``Rand``.

    Attributes:
        options: Dictionary of options.
    """

    options: list[str] | list[rand.RandOption] = None

    def build(self):
        """
        Builds ``RandBuilder`` into ``Rand``.

        Returns:
            ``Rand`` for ``RandBuilder``.
        """

        options = []
        for item in self.options:
            if isinstance(item, rand.RandOption):
                options.append(item)
            elif isinstance(item, str):
                options.append(rand.RandOption.from_mcnp(item))
            else:
                options.append(item.build())
        options = types.Tuple(options)

        return Rand(
            options=options,
        )
