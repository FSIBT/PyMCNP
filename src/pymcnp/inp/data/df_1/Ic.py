import re
import typing


from .option_ import Df_1Option_
from ....utils import types
from ....utils import errors


class Ic(Df_1Option_, keyword='ic'):
    """
    Represents INP ic elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'function': types.Integer,
    }

    _REGEX = re.compile(rf'\Aic( {types.Integer._REGEX.pattern})\Z')

    def __init__(self, function: types.Integer):
        """
        Initializes ``Ic``.

        Parameters:
            function: Standard dose function.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if function is None or function not in {10, 20, 31, 32, 33, 34, 35, 40, 99}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, function)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                function,
            ]
        )

        self.function: typing.Final[types.Integer] = function
