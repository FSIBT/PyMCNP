import re
import typing
import dataclasses


from ._option import PertOption
from ....utils import types
from ....utils import errors


class Mat(PertOption):
    """
    Represents INP mat elements.

    Attributes:
        material: Material number to fill cells.
    """

    _ATTRS = {
        'material': types.Integer,
    }

    _REGEX = re.compile(rf'\Amat( {types.Integer._REGEX.pattern})\Z')

    def __init__(self, material: types.Integer):
        """
        Initializes ``Mat``.

        Parameters:
            material: Material number to fill cells.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if material is None or not (0 <= material.value <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, material)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                material,
            ]
        )

        self.material: typing.Final[types.Integer] = material


@dataclasses.dataclass
class MatBuilder:
    """
    Builds ``Mat``.

    Attributes:
        material: Material number to fill cells.
    """

    material: str | int | types.Integer

    def build(self):
        """
        Builds ``MatBuilder`` into ``Mat``.

        Returns:
            ``Mat`` for ``MatBuilder``.
        """

        material = self.material
        if isinstance(self.material, types.Integer):
            material = self.material
        elif isinstance(self.material, int):
            material = types.Integer(self.material)
        elif isinstance(self.material, str):
            material = types.Integer.from_mcnp(self.material)

        return Mat(
            material=material,
        )
