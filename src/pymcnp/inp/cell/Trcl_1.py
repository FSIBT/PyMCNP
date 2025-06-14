import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Trcl_1(_option.CellOption):
    """
    Represents INP trcl variation #1 elements.

    Attributes:
        transformation: Cell transformation..
    """

    _KEYWORD = 'trcl'

    _ATTRS = {
        'transformation': types.Transformation_0,
    }

    _REGEX = re.compile(rf'\Atrcl( {types.Transformation_0._REGEX.pattern[2:-2]})\Z')

    def __init__(self, transformation: types.Transformation_0):
        """
        Initializes ``Trcl_1``.

        Parameters:
            transformation: Cell transformation..

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if transformation is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, transformation)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                transformation,
            ]
        )

        self.transformation: typing.Final[types.Transformation_0] = transformation


@dataclasses.dataclass
class TrclBuilder_1(_option.CellOptionBuilder):
    """
    Builds ``Trcl_1``.

    Attributes:
        transformation: Cell transformation..
    """

    transformation: str | types.Transformation_0

    def build(self):
        """
        Builds ``TrclBuilder_1`` into ``Trcl_1``.

        Returns:
            ``Trcl_1`` for ``TrclBuilder_1``.
        """

        transformation = self.transformation
        if isinstance(self.transformation, types.Transformation_0):
            transformation = self.transformation
        elif isinstance(self.transformation, str):
            transformation = types.Transformation_0.from_mcnp(self.transformation)

        return Trcl_1(
            transformation=transformation,
        )

    @staticmethod
    def unbuild(ast: Trcl_1):
        """
        Unbuilds ``Trcl_1`` into ``TrclBuilder_1``

        Returns:
            ``TrclBuilder_1`` for ``Trcl_1``.
        """

        return TrclBuilder_1(
            transformation=copy.deepcopy(ast.transformation),
        )
