import re
import typing
import dataclasses


from . import tropt
from .option_ import DataOption_
from ...utils import types


class Tropt(DataOption_, keyword='tropt'):
    """
    Represents INP tropt elements.

    Attributes:
        options: Dictionary of options.
    """

    _ATTRS = {
        'options': types.Tuple[tropt.TroptOption_],
    }

    _REGEX = re.compile(rf'\Atropt((?: (?:{tropt.TroptOption_._REGEX.pattern}))+?)?\Z')

    def __init__(self, options: types.Tuple[tropt.TroptOption_] = None):
        """
        Initializes ``Tropt``.

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

        self.options: typing.Final[types.Tuple[tropt.TroptOption_]] = options


@dataclasses.dataclass
class TroptBuilder:
    """
    Builds ``Tropt``.

    Attributes:
        options: Dictionary of options.
    """

    options: list[str] | list[tropt.TroptOption_] = None

    def build(self):
        """
        Builds ``TroptBuilder`` into ``Tropt``.

        Returns:
            ``Tropt`` for ``TroptBuilder``.
        """

        options = []
        for item in self.options:
            if isinstance(item, tropt.TroptOption_):
                options.append(item)
            elif isinstance(item, str):
                options.append(tropt.TroptOption_.from_mcnp(item))
            else:
                options.append(item.build())
        options = types.Tuple(options)

        return Tropt(
            options=options,
        )
