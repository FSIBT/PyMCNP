import re
import copy
import typing
import dataclasses


from ._option import FmeshOption
from ....utils import types
from ....utils import errors


class Tr(FmeshOption):
    """
    Represents INP tr elements.

    Attributes:
        number: Transformation applied to the mesh.
    """

    _KEYWORD = 'tr'

    _ATTRS = {
        'number': types.Integer,
    }

    _REGEX = re.compile(rf'\Atr( {types.Integer._REGEX.pattern})\Z')

    def __init__(self, number: types.Integer):
        """
        Initializes ``Tr``.

        Parameters:
            number: Transformation applied to the mesh.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if number is None or not (1 <= number.value <= 999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, number)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                number,
            ]
        )

        self.number: typing.Final[types.Integer] = number


@dataclasses.dataclass
class TrBuilder:
    """
    Builds ``Tr``.

    Attributes:
        number: Transformation applied to the mesh.
    """

    number: str | int | types.Integer

    def build(self):
        """
        Builds ``TrBuilder`` into ``Tr``.

        Returns:
            ``Tr`` for ``TrBuilder``.
        """

        number = self.number
        if isinstance(self.number, types.Integer):
            number = self.number
        elif isinstance(self.number, int):
            number = types.Integer(self.number)
        elif isinstance(self.number, str):
            number = types.Integer.from_mcnp(self.number)

        return Tr(
            number=number,
        )

    @staticmethod
    def unbuild(ast: Tr):
        """
        Unbuilds ``Tr`` into ``TrBuilder``

        Returns:
            ``TrBuilder`` for ``Tr``.
        """

        return Tr(
            number=copy.deepcopy(ast.number),
        )
