import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Trcl_4(_option.CellOption):
    """
    Represents INP trcl variation #4 elements.

    Attributes:
        transformation: Cell transformation..
    """

    _KEYWORD = 'trcl'

    _ATTRS = {
        'transformation': types.Transformation_3,
    }

    _REGEX = re.compile(rf'\Atrcl( {types.Transformation_3._REGEX.pattern[2:-2]})\Z')

    def __init__(self, transformation: types.Transformation_3):
        """
        Initializes ``Trcl_4``.

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

        self.transformation: typing.Final[types.Transformation_3] = transformation


@dataclasses.dataclass
class TrclBuilder_4(_option.CellOptionBuilder):
    """
    Builds ``Trcl_4``.

    Attributes:
        transformation: Cell transformation..
    """

    transformation: str | types.Transformation_3

    def build(self):
        """
        Builds ``TrclBuilder_4`` into ``Trcl_4``.

        Returns:
            ``Trcl_4`` for ``TrclBuilder_4``.
        """

        transformation = self.transformation
        if isinstance(self.transformation, types.Transformation_3):
            transformation = self.transformation
        elif isinstance(self.transformation, str):
            transformation = types.Transformation_3.from_mcnp(self.transformation)

        return Trcl_4(
            transformation=transformation,
        )

    @staticmethod
    def unbuild(ast: Trcl_4):
        """
        Unbuilds ``Trcl_4`` into ``TrclBuilder_4``

        Returns:
            ``TrclBuilder_4`` for ``Trcl_4``.
        """

        return TrclBuilder_4(
            transformation=copy.deepcopy(ast.transformation),
        )
