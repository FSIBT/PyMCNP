import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Sp_1(_option.DataOption):
    """
    Represents INP sp variation #1 elements.

    Attributes:
        function: Built-in function designator.
        a: Built-in function parameter #1.
        b: Built-in function parameter #2.
    """

    _KEYWORD = 'sp'

    _ATTRS = {
        'function': types.Integer,
        'a': types.Real,
        'b': types.Real,
    }

    _REGEX = re.compile(rf'\Asp( {types.Integer._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})?\Z')

    def __init__(self, function: types.Integer, a: types.Real, b: types.Real = None):
        """
        Initializes ``Sp_1``.

        Parameters:
            function: Built-in function designator.
            a: Built-in function parameter #1.
            b: Built-in function parameter #2.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if function is None or function.value not in {-2, -3, -4, -5, -6, -7, -21, -31, -41}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, function)
        if a is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, a)

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


@dataclasses.dataclass
class SpBuilder_1(_option.DataOptionBuilder):
    """
    Builds ``Sp_1``.

    Attributes:
        function: Built-in function designator.
        a: Built-in function parameter #1.
        b: Built-in function parameter #2.
    """

    function: str | int | types.Integer
    a: str | float | types.Real
    b: str | float | types.Real = None

    def build(self):
        """
        Builds ``SpBuilder_1`` into ``Sp_1``.

        Returns:
            ``Sp_1`` for ``SpBuilder_1``.
        """

        function = self.function
        if isinstance(self.function, types.Integer):
            function = self.function
        elif isinstance(self.function, int):
            function = types.Integer(self.function)
        elif isinstance(self.function, str):
            function = types.Integer.from_mcnp(self.function)

        a = self.a
        if isinstance(self.a, types.Real):
            a = self.a
        elif isinstance(self.a, float) or isinstance(self.a, int):
            a = types.Real(self.a)
        elif isinstance(self.a, str):
            a = types.Real.from_mcnp(self.a)

        b = self.b
        if isinstance(self.b, types.Real):
            b = self.b
        elif isinstance(self.b, float) or isinstance(self.b, int):
            b = types.Real(self.b)
        elif isinstance(self.b, str):
            b = types.Real.from_mcnp(self.b)

        return Sp_1(
            function=function,
            a=a,
            b=b,
        )

    @staticmethod
    def unbuild(ast: Sp_1):
        """
        Unbuilds ``Sp_1`` into ``SpBuilder_1``

        Returns:
            ``SpBuilder_1`` for ``Sp_1``.
        """

        return SpBuilder_1(
            function=copy.deepcopy(ast.function),
            a=copy.deepcopy(ast.a),
            b=copy.deepcopy(ast.b),
        )
