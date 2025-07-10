import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Mat(_option.LikeOption):
    """
    Represents INP mat elements.

    Attributes:
        material: Cell material.
    """

    _KEYWORD = 'mat'

    _ATTRS = {
        'material': types.Integer,
    }

    _REGEX = re.compile(rf'\Amat( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, material: types.Integer):
        """
        Initializes ``Mat``.

        Parameters:
            material: Cell material.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if material is None or not (0 <= material <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, material)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                material,
            ]
        )

        self.material: typing.Final[types.Integer] = material


@dataclasses.dataclass
class MatBuilder(_option.LikeOptionBuilder):
    """
    Builds ``Mat``.

    Attributes:
        material: Cell material.
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

    @staticmethod
    def unbuild(ast: Mat):
        """
        Unbuilds ``Mat`` into ``MatBuilder``

        Returns:
            ``MatBuilder`` for ``Mat``.
        """

        return MatBuilder(
            material=copy.deepcopy(ast.material),
        )
