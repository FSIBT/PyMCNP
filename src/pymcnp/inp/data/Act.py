import re
import typing


from . import act
from .option_ import DataOption_
from ...utils import types


class Act(DataOption_, keyword='act'):
    """
    Represents INP act elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'options': types.Tuple[act.ActOption_],
    }

    _REGEX = re.compile(rf'act(( ({act.ActOption_._REGEX.pattern}))+)?')

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
