import re
import typing
import dataclasses


from ._option import CellOption
from ...utils import types
from ...utils import errors


class Trcl_1(CellOption, keyword='trcl'):
    """
    Represents INP trcl variation #1 elements.

    Attributes:
        transformation: Cell transformation..
    """

    _ATTRS = {
        'transformation': types.Transformation_0,
    }

    _REGEX = re.compile(rf'\Atrcl( {types.Transformation_0._REGEX.pattern})\Z')

    def __init__(self, transformation: types.Transformation_0):
        """
        Initializes ``Trcl_1``.

        Parameters:
            transformation: Cell transformation..

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if transformation is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, transformation)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                transformation,
            ]
        )

        self.transformation: typing.Final[types.Transformation_0] = transformation


@dataclasses.dataclass
class TrclBuilder_1:
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

        if isinstance(self.transformation, types.Transformation_0):
            transformation = self.transformation
        elif isinstance(self.transformation, str):
            transformation = types.Transformation_0.from_mcnp(self.transformation)

        return Trcl_1(
            transformation=transformation,
        )
