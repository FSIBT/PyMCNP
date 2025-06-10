import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Ic(_option.DfOption_1):
    """
    Represents INP ic elements.

    Attributes:
        function: Standard dose function.
    """

    _KEYWORD = 'ic'

    _ATTRS = {
        'function': types.Integer,
    }

    _REGEX = re.compile(rf'\Aic( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, function: types.Integer):
        """
        Initializes ``Ic``.

        Parameters:
            function: Standard dose function.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if function is None or not (isinstance(function.value, types.Jump) or function.value in {10, 20, 31, 32, 33, 34, 35, 40, 99}):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, function)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                function,
            ]
        )

        self.function: typing.Final[types.Integer] = function


@dataclasses.dataclass
class IcBuilder(_option.DfOptionBuilder_1):
    """
    Builds ``Ic``.

    Attributes:
        function: Standard dose function.
    """

    function: str | int | types.Integer

    def build(self):
        """
        Builds ``IcBuilder`` into ``Ic``.

        Returns:
            ``Ic`` for ``IcBuilder``.
        """

        function = self.function
        if isinstance(self.function, types.Integer):
            function = self.function
        elif isinstance(self.function, int):
            function = types.Integer(self.function)
        elif isinstance(self.function, str):
            function = types.Integer.from_mcnp(self.function)

        return Ic(
            function=function,
        )

    @staticmethod
    def unbuild(ast: Ic):
        """
        Unbuilds ``Ic`` into ``IcBuilder``

        Returns:
            ``IcBuilder`` for ``Ic``.
        """

        return IcBuilder(
            function=copy.deepcopy(ast.function),
        )
