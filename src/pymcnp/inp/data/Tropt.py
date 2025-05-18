import re
import typing
import dataclasses


from . import tropt
from ._option import DataOption
from ...utils import types


class Tropt(DataOption):
    """
    Represents INP tropt elements.

    Attributes:
        options: Dictionary of options.
    """

    _ATTRS = {
        'options': types.Tuple[tropt.TroptOption],
    }

    _REGEX = re.compile(rf'\Atropt((?: (?:{tropt.TroptOption._REGEX.pattern}))+?)?\Z')

    def __init__(self, options: types.Tuple[tropt.TroptOption] = None):
        """
        Initializes ``Tropt``.

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

        self.options: typing.Final[types.Tuple[tropt.TroptOption]] = options


@dataclasses.dataclass
class TroptBuilder:
    """
    Builds ``Tropt``.

    Attributes:
        options: Dictionary of options.
    """

    options: list[str] | list[tropt.TroptOption] = None

    def build(self):
        """
        Builds ``TroptBuilder`` into ``Tropt``.

        Returns:
            ``Tropt`` for ``TroptBuilder``.
        """

        if self.options:
            options = []
            for item in self.options:
                if isinstance(item, tropt.TroptOption):
                    options.append(item)
                elif isinstance(item, str):
                    options.append(tropt.TroptOption.from_mcnp(item))
                else:
                    options.append(item.build())
            options = types.Tuple(options)
        else:
            options = None

        return Tropt(
            options=options,
        )
