import re
import typing
import dataclasses


from ._option import Df_1Option
from ....utils import types
from ....utils import errors


class Ic(Df_1Option, keyword='ic'):
    """
    Represents INP ic elements.

    Attributes:
        function: Standard dose function.
    """

    _ATTRS = {
        'function': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Aic( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, function: types.IntegerOrJump):
        """
        Initializes ``Ic``.

        Parameters:
            function: Standard dose function.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if function is None or function.value not in {10, 20, 31, 32, 33, 34, 35, 40, 99}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, function)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                function,
            ]
        )

        self.function: typing.Final[types.IntegerOrJump] = function


@dataclasses.dataclass
class IcBuilder:
    """
    Builds ``Ic``.

    Attributes:
        function: Standard dose function.
    """

    function: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``IcBuilder`` into ``Ic``.

        Returns:
            ``Ic`` for ``IcBuilder``.
        """

        if isinstance(self.function, types.Integer):
            function = self.function
        elif isinstance(self.function, int):
            function = types.IntegerOrJump(self.function)
        elif isinstance(self.function, str):
            function = types.IntegerOrJump.from_mcnp(self.function)

        return Ic(
            function=function,
        )
