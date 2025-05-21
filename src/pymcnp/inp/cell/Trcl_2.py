import re
import copy
import typing
import dataclasses


from ._option import CellOption
from ...utils import types
from ...utils import errors


class Trcl_2(CellOption):
    """
    Represents INP trcl variation #2 elements.

    Attributes:
        transformation: Cell transformation..
    """

    _KEYWORD = 'trcl'

    _ATTRS = {
        'transformation': types.Transformation_1,
    }

    _REGEX = re.compile(rf'\Atrcl( {types.Transformation_1._REGEX.pattern})\Z')

    def __init__(self, transformation: types.Transformation_1):
        """
        Initializes ``Trcl_2``.

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

        self.transformation: typing.Final[types.Transformation_1] = transformation


@dataclasses.dataclass
class TrclBuilder_2:
    """
    Builds ``Trcl_2``.

    Attributes:
        transformation: Cell transformation..
    """

    transformation: str | types.Transformation_1

    def build(self):
        """
        Builds ``TrclBuilder_2`` into ``Trcl_2``.

        Returns:
            ``Trcl_2`` for ``TrclBuilder_2``.
        """

        transformation = self.transformation
        if isinstance(self.transformation, types.Transformation_1):
            transformation = self.transformation
        elif isinstance(self.transformation, str):
            transformation = types.Transformation_1.from_mcnp(self.transformation)

        return Trcl_2(
            transformation=transformation,
        )

    @staticmethod
    def unbuild(ast: Trcl_2):
        """
        Unbuilds ``Trcl_2`` into ``TrclBuilder_2``

        Returns:
            ``TrclBuilder_2`` for ``Trcl_2``.
        """

        return Trcl_2(
            transformation=copy.deepcopy(ast.transformation),
        )
