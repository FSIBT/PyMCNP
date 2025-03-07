import re
import typing


from .option_ import CellOption_
from ...utils import types
from ...utils import errors


class Lat(CellOption_, keyword='lat'):
    """
    Represents INP lat elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'shape': types.Integer,
    }

    _REGEX = re.compile(rf'lat( {types.Integer._REGEX.pattern})')

    def __init__(self, shape: types.Integer):
        """
        Initializes ``Lat``.

        Parameters:
            shape: Cell lattice shape.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if shape is None or shape.value not in {1, 2}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, shape)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                shape,
            ]
        )

        self.shape: typing.Final[types.Integer] = shape
