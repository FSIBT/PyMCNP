import re
import typing
import dataclasses


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Sb_1(DataOption_, keyword='sb'):
    """
    Represents INP sb variation #1 elements.

    Attributes:
        function: Built-in function designator.
        a: Built-in function parameter #1.
        b: Built-in function parameter #2.
    """

    _ATTRS = {
        'function': types.IntegerOrJump,
        'a': types.RealOrJump,
        'b': types.RealOrJump,
    }

    _REGEX = re.compile(
        rf'\Asb( {types.IntegerOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})?\Z'
    )

    def __init__(
        self, function: types.IntegerOrJump, a: types.RealOrJump, b: types.RealOrJump = None
    ):
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

        self.function: typing.Final[types.IntegerOrJump] = function
        self.a: typing.Final[types.RealOrJump] = a
        self.b: typing.Final[types.RealOrJump] = b


@dataclasses.dataclass
class SbBuilder_1:
    """
    Builds ``Sb_1``.

    Attributes:
        function: Built-in function designator.
        a: Built-in function parameter #1.
        b: Built-in function parameter #2.
    """

    function: str | int | types.IntegerOrJump
    a: str | float | types.RealOrJump
    b: str | float | types.RealOrJump = None

    def build(self):
        """
        Builds ``SbBuilder_1`` into ``Sb_1``.

        Returns:
            ``Sb_1`` for ``SbBuilder_1``.
        """

        if isinstance(self.function, types.Integer):
            function = self.function
        elif isinstance(self.function, int):
            function = types.IntegerOrJump(self.function)
        elif isinstance(self.function, str):
            function = types.IntegerOrJump.from_mcnp(self.function)

        if isinstance(self.a, types.Real):
            a = self.a
        elif isinstance(self.a, float) or isinstance(self.a, int):
            a = types.RealOrJump(self.a)
        elif isinstance(self.a, str):
            a = types.RealOrJump.from_mcnp(self.a)

        b = None
        if isinstance(self.b, types.Real):
            b = self.b
        elif isinstance(self.b, float) or isinstance(self.b, int):
            b = types.RealOrJump(self.b)
        elif isinstance(self.b, str):
            b = types.RealOrJump.from_mcnp(self.b)

        return Sb_1(
            function=function,
            a=a,
            b=b,
        )
