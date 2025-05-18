import re
import typing
import dataclasses


from ._option import CellOption
from ...utils import types
from ...utils import errors


class Trcl_4(CellOption):
    """
    Represents INP trcl variation #4 elements.

    Attributes:
        transformation: Cell transformation..
    """

    _ATTRS = {
        'transformation': types.Transformation_3,
    }

    _REGEX = re.compile(rf'\Atrcl( {types.Transformation_3._REGEX.pattern})\Z')

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
class TrclBuilder_4:
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
