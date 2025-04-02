import re
import typing


from . import tropt
from .option_ import DataOption_
from ...utils import types


class Tropt(DataOption_, keyword='tropt'):
    """
    Represents INP tropt elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
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
