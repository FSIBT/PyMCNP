import re
import typing


from . import var
from .option_ import DataOption_
from ...utils import types


class Var(DataOption_, keyword='var'):
    """
    Represents INP var elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'options': types.Tuple[var.VarOption_],
    }

    _REGEX = re.compile(rf'\Avar((?: (?:{var.VarOption_._REGEX.pattern}))+?)?\Z')

    def __init__(self, options: types.Tuple[var.VarOption_] = None):
        """
        Initializes ``Var``.

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

        self.options: typing.Final[types.Tuple[var.VarOption_]] = options
