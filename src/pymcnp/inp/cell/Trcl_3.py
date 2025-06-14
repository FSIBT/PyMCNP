import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Trcl_3(_option.CellOption):
    """
    Represents INP trcl variation #3 elements.

    Attributes:
        transformation: Cell transformation..
    """

    _KEYWORD = 'trcl'

    _ATTRS = {
        'transformation': types.Transformation_2,
    }

    _REGEX = re.compile(rf'\Atrcl( {types.Transformation_2._REGEX.pattern[2:-2]})\Z')

    def __init__(self, transformation: types.Transformation_2):
        """
        Initializes ``Trcl_3``.

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

        self.transformation: typing.Final[types.Transformation_2] = transformation


@dataclasses.dataclass
class TrclBuilder_3(_option.CellOptionBuilder):
    """
    Builds ``Trcl_3``.

    Attributes:
        transformation: Cell transformation..
    """

    transformation: str | types.Transformation_2

    def build(self):
        """
        Builds ``TrclBuilder_3`` into ``Trcl_3``.

        Returns:
            ``Trcl_3`` for ``TrclBuilder_3``.
        """

        transformation = self.transformation
        if isinstance(self.transformation, types.Transformation_2):
            transformation = self.transformation
        elif isinstance(self.transformation, str):
            transformation = types.Transformation_2.from_mcnp(self.transformation)

        return Trcl_3(
            transformation=transformation,
        )

    @staticmethod
    def unbuild(ast: Trcl_3):
        """
        Unbuilds ``Trcl_3`` into ``TrclBuilder_3``

        Returns:
            ``TrclBuilder_3`` for ``Trcl_3``.
        """

        return TrclBuilder_3(
            transformation=copy.deepcopy(ast.transformation),
        )
