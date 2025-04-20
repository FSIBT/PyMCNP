import re
import typing
import dataclasses


from .option_ import CellOption_
from ...utils import types
from ...utils import errors


class Trcl_2(CellOption_, keyword='trcl'):
    """
    Represents INP trcl variation #2 elements.

    Attributes:
        transformation: Cell transformation..
    """

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
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if transformation is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, transformation)

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

        if isinstance(self.transformation, types.Transformation_1):
            transformation = self.transformation
        elif isinstance(self.transformation, str):
            transformation = types.Transformation_1.from_mcnp(self.transformation)

        return Trcl_2(
            transformation=transformation,
        )
