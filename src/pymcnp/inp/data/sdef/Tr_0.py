import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Tr_0(_option.SdefOption):
    """
    Represents INP tr variation #0 elements.

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
        Initializes ``Tr_0``.

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
class TrBuilder_0(_option.SdefOptionBuilder):
    """
    Builds ``Tr_0``.

    Attributes:
        number: Particle weight.
    """

    number: str | int | types.Integer

    def build(self):
        """
        Builds ``TrBuilder_0`` into ``Tr_0``.

        Returns:
            ``Tr_0`` for ``TrBuilder_0``.
        """

        number = self.number
        if isinstance(self.number, types.Integer):
            number = self.number
        elif isinstance(self.number, int):
            number = types.Integer(self.number)
        elif isinstance(self.number, str):
            number = types.Integer.from_mcnp(self.number)

        return Tr_0(
            number=number,
        )

    @staticmethod
    def unbuild(ast: Tr_0):
        """
        Unbuilds ``Tr_0`` into ``TrBuilder_0``

        Returns:
            ``TrBuilder_0`` for ``Tr_0``.
        """

        return TrBuilder_0(
            number=copy.deepcopy(ast.number),
        )
