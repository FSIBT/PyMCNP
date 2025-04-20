import re
import typing
import dataclasses


from . import rand
from .option_ import DataOption_
from ...utils import types


class Rand(DataOption_, keyword='rand'):
    """
    Represents INP rand elements.

    Attributes:
        options: Dictionary of options.
    """

    _ATTRS = {
        'options': types.Tuple[rand.RandOption_],
    }

    _REGEX = re.compile(rf'\Arand((?: (?:{rand.RandOption_._REGEX.pattern}))+?)?\Z')

    def __init__(self, options: types.Tuple[rand.RandOption_] = None):
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

        self.options: typing.Final[types.Tuple[rand.RandOption_]] = options


@dataclasses.dataclass
class RandBuilder:
    """
    Builds ``Rand``.

    Attributes:
        options: Dictionary of options.
    """

    options: list[str] | list[rand.RandOption_] = None

    def build(self):
        """
        Builds ``RandBuilder`` into ``Rand``.

        Returns:
            ``Rand`` for ``RandBuilder``.
        """

        options = []
        for item in self.options:
            if isinstance(item, rand.RandOption_):
                options.append(item)
            elif isinstance(item, str):
                options.append(rand.RandOption_.from_mcnp(item))
            else:
                options.append(item.build())
        options = types.Tuple(options)

        return Rand(
            options=options,
        )
