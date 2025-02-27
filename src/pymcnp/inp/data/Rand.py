import re
import typing


from . import rand
from .option_ import DataOption_
from ...utils import types


class Rand(DataOption_, keyword='rand'):
    """
    Represents INP rand elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'options': types.Tuple[rand.RandOption_],
    }

    _REGEX = re.compile(rf'rand(( ({rand.RandOption_._REGEX.pattern}))+)?')

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
