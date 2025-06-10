import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Tr_1(_option.SdefOption):
    """
    Represents INP tr variation #1 elements.

    Attributes:
        number: Particle weight.
    """

    _KEYWORD = 'tr'

    _ATTRS = {
        'number': types.Integer,
    }

    _REGEX = re.compile(rf'\Atr( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, number: types.Integer):
        """
        Initializes ``Tr_1``.

        Parameters:
            number: Particle weight.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if number is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, number)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                number,
            ]
        )

        self.number: typing.Final[types.Integer] = number


@dataclasses.dataclass
class TrBuilder_1(_option.SdefOptionBuilder):
    """
    Builds ``Tr_1``.

    Attributes:
        number: Particle weight.
    """

    number: str | int | types.Integer

    def build(self):
        """
        Builds ``TrBuilder_1`` into ``Tr_1``.

        Returns:
            ``Tr_1`` for ``TrBuilder_1``.
        """

        number = self.number
        if isinstance(self.number, types.Integer):
            number = self.number
        elif isinstance(self.number, int):
            number = types.Integer(self.number)
        elif isinstance(self.number, str):
            number = types.Integer.from_mcnp(self.number)

        return Tr_1(
            number=number,
        )

    @staticmethod
    def unbuild(ast: Tr_1):
        """
        Unbuilds ``Tr_1`` into ``TrBuilder_1``

        Returns:
            ``TrBuilder_1`` for ``Tr_1``.
        """

        return TrBuilder_1(
            number=copy.deepcopy(ast.number),
        )
