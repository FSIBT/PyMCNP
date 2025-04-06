import re
import typing


from .option_ import CellOption_
from ...utils import types
from ...utils import errors


class Trcl_4(CellOption_, keyword='trcl'):
    """
    Represents INP trcl_4 elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
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
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if transformation is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, transformation)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                transformation,
            ]
        )

        self.transformation: typing.Final[types.Transformation_3] = transformation
