import re
import copy
import typing
import dataclasses


from ._option import CellOption
from ...utils import types
from ...utils import errors


class Trcl_0(CellOption):
    """
    Represents INP trcl variation #0 elements.

    Attributes:
        transformation: Cell transformation number.
    """

    _KEYWORD = 'trcl'

    _ATTRS = {
        'transformation': types.Integer,
    }

    _REGEX = re.compile(rf'\Atrcl( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, transformation: types.Integer):
        """
        Initializes ``Trcl_0``.

        Parameters:
            transformation: Cell transformation number.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if transformation is None or not (0 <= transformation.value <= 999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, transformation)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                transformation,
            ]
        )

        self.transformation: typing.Final[types.Integer] = transformation


@dataclasses.dataclass
class TrclBuilder_0:
    """
    Builds ``Trcl_0``.

    Attributes:
        transformation: Cell transformation number.
    """

    transformation: str | int | types.Integer

    def build(self):
        """
        Builds ``TrclBuilder_0`` into ``Trcl_0``.

        Returns:
            ``Trcl_0`` for ``TrclBuilder_0``.
        """

        transformation = self.transformation
        if isinstance(self.transformation, types.Integer):
            transformation = self.transformation
        elif isinstance(self.transformation, int):
            transformation = types.Integer(self.transformation)
        elif isinstance(self.transformation, str):
            transformation = types.Integer.from_mcnp(self.transformation)

        return Trcl_0(
            transformation=transformation,
        )

    @staticmethod
    def unbuild(ast: Trcl_0):
        """
        Unbuilds ``Trcl_0`` into ``TrclBuilder_0``

        Returns:
            ``TrclBuilder_0`` for ``Trcl_0``.
        """

        return Trcl_0(
            transformation=copy.deepcopy(ast.transformation),
        )
