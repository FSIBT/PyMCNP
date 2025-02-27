import re
import typing


from . import kopts
from .option_ import DataOption_
from ...utils import types


class Kopts(DataOption_, keyword='kopts'):
    """
    Represents INP kopts elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'options': types.Tuple[kopts.KoptsOption_],
    }

    _REGEX = re.compile(rf'kopts(( ({kopts.KoptsOption_._REGEX.pattern}))+)?')

    def __init__(self, options: types.Tuple[kopts.KoptsOption_] = None):
        """
        Initializes ``Kopts``.

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

        self.options: typing.Final[types.Tuple[kopts.KoptsOption_]] = options
