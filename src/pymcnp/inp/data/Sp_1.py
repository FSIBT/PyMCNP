import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Sp_1(DataOption_, keyword='sp'):
    """
    Represents INP sp_1 elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'function': types.Integer,
        'a': types.Real,
        'b': types.Real,
    }

    _REGEX = re.compile(r'sp( \S+)( \S+)( \S+)?')

    def __init__(self, function: types.Integer, a: types.Real, b: types.Real = None):
        """
        Initializes ``Sp_1``.

        Parameters:
            function: Built-in function designator.
            a: Built-in function parameter #1.
            b: Built-in function parameter #2.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if function is None or function not in {-2, -3, -4, -5, -6, -7, -21, -31, -41}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, function)
        if a is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, a)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                function,
                a,
                b,
            ]
        )

        self.function: typing.Final[types.Integer] = function
        self.a: typing.Final[types.Real] = a
        self.b: typing.Final[types.Real] = b
