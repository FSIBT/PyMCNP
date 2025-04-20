import re
import typing
import dataclasses


from . import act
from .option_ import DataOption_
from ...utils import types


class Act(DataOption_, keyword='act'):
    """
    Represents INP act elements.

    Attributes:
        options: Dictionary of options.
    """

    _ATTRS = {
        'options': types.Tuple[act.ActOption_],
    }

    _REGEX = re.compile(rf'\Aact((?: (?:{act.ActOption_._REGEX.pattern}))+?)?\Z')

    def __init__(self, options: types.Tuple[act.ActOption_] = None):
        """
        Initializes ``Act``.

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

        self.options: typing.Final[types.Tuple[act.ActOption_]] = options


@dataclasses.dataclass
class ActBuilder:
    """
    Builds ``Act``.

    Attributes:
        options: Dictionary of options.
    """

    options: list[str] | list[act.ActOption_] = None

    def build(self):
        """
        Builds ``ActBuilder`` into ``Act``.

        Returns:
            ``Act`` for ``ActBuilder``.
        """

        options = []
        for item in self.options:
            if isinstance(item, act.ActOption_):
                options.append(item)
            elif isinstance(item, str):
                options.append(act.ActOption_.from_mcnp(item))
            else:
                options.append(item.build())
        options = types.Tuple(options)

        return Act(
            options=options,
        )
