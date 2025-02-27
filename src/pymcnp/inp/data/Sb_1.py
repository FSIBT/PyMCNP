import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Sb_1(DataOption_, keyword='sb'):
    """
    Represents INP sb_1 elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'function': types.Integer,
        'a': types.Real,
        'b': types.Real,
    }

    _REGEX = re.compile(r'sb( \S+)( \S+)( \S+)?')

    def __init__(self, function: types.Integer, a: types.Real, b: types.Real = None):
        """
        Initializes ``Sb_1``.

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
