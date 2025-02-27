import re
import typing


from .option_ import DataOption_
from ...utils import types


class Histp(DataOption_, keyword='histp'):
    """
    Represents INP histp elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'lhist': types.Integer,
        'cells': types.Tuple[types.Integer],
    }

    _REGEX = re.compile(r'histp( \S+)?(( \S+)+)?')

    def __init__(self, lhist: types.Integer = None, cells: types.Tuple[types.Integer] = None):
        """
        Initializes ``Histp``.

        Parameters:
            lhist: Number of words written to a HISTP file.
            cells: Cell numbers.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                lhist,
                cells,
            ]
        )

        self.lhist: typing.Final[types.Integer] = lhist
        self.cells: typing.Final[types.Tuple[types.Integer]] = cells
