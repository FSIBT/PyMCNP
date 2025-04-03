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
        'lhist': types.IntegerOrJump,
        'cells': types.Tuple[types.IntegerOrJump],
    }

    _REGEX = re.compile(
        rf'\Ahistp( {types.IntegerOrJump._REGEX.pattern})?((?: {types.IntegerOrJump._REGEX.pattern})+?)?\Z'
    )

    def __init__(
        self, lhist: types.IntegerOrJump = None, cells: types.Tuple[types.IntegerOrJump] = None
    ):
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

        self.lhist: typing.Final[types.IntegerOrJump] = lhist
        self.cells: typing.Final[types.Tuple[types.IntegerOrJump]] = cells
