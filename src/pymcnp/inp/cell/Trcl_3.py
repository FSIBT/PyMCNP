import re
import typing
import dataclasses


from ._option import CellOption
from ...utils import types
from ...utils import errors


class Trcl_3(CellOption):
    """
    Represents INP trcl variation #3 elements.

    Attributes:
        transformation: Cell transformation..
    """

    _ATTRS = {
        'transformation': types.Transformation_2,
    }

    _REGEX = re.compile(rf'\Atrcl( {types.Transformation_2._REGEX.pattern})\Z')

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
class TrclBuilder_3:
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
