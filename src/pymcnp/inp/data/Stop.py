import re
import typing


from . import stop
from .option_ import DataOption_
from ...utils import types


class Stop(DataOption_, keyword='stop'):
    """
    Represents INP stop elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'options': types.Tuple[stop.StopOption_],
    }

    _REGEX = re.compile(rf'stop(( ({stop.StopOption_._REGEX.pattern}))+)?')

    def __init__(self, options: types.Tuple[stop.StopOption_] = None):
        """
        Initializes ``Stop``.

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

        self.options: typing.Final[types.Tuple[stop.StopOption_]] = options
