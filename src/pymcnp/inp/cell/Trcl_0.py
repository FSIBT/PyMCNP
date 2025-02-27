import re
import typing


from .option_ import CellOption_
from ...utils import types
from ...utils import errors


class Trcl_0(CellOption_, keyword='trcl'):
    """
    Represents INP trcl_0 elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'transformation': types.Integer,
    }

    _REGEX = re.compile(r'trcl( \S+)')

    def __init__(self, transformation: types.Integer):
        """
        Initializes ``Trcl_0``.

        Parameters:
            transformation: Cell transformation number.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if transformation is None or not (1 <= transformation <= 999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, transformation)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                transformation,
            ]
        )

        self.transformation: typing.Final[types.Integer] = transformation
