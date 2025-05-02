import re
import typing
import dataclasses


from ._option import CellOption
from ...utils import types
from ...utils import errors


class Trcl_5(CellOption):
    """
    Represents INP trcl variation #5 elements.

    Attributes:
        transformation: Cell transformation..
    """

    _ATTRS = {
        'transformation': types.Transformation_4,
    }

    _REGEX = re.compile(rf'\Atrcl( {types.Transformation_4._REGEX.pattern})\Z')

    def __init__(self, transformation: types.Transformation_4):
        """
        Initializes ``Trcl_5``.

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

        self.transformation: typing.Final[types.Transformation_4] = transformation


@dataclasses.dataclass
class TrclBuilder_5:
    """
    Builds ``Trcl_5``.

    Attributes:
        transformation: Cell transformation..
    """

    transformation: str | types.Transformation_4

    def build(self):
        """
        Builds ``TrclBuilder_5`` into ``Trcl_5``.

        Returns:
            ``Trcl_5`` for ``TrclBuilder_5``.
        """

        if isinstance(self.transformation, types.Transformation_4):
            transformation = self.transformation
        elif isinstance(self.transformation, str):
            transformation = types.Transformation_4.from_mcnp(self.transformation)

        return Trcl_5(
            transformation=transformation,
        )
