import re
import typing


from . import ssw
from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Ssw(DataOption_, keyword='ssw'):
    """
    Represents INP ssw elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'surfaces': types.Tuple[types.IntegerOrJump],
        'cells': types.Tuple[types.IntegerOrJump],
        'options': types.Tuple[ssw.SswOption_],
    }

    _REGEX = re.compile(
        rf'\Assw((?: {types.IntegerOrJump._REGEX.pattern})+?)((?: {types.IntegerOrJump._REGEX.pattern})+?)((?: (?:{ssw.SswOption_._REGEX.pattern}))+?)?\Z'
    )

    def __init__(
        self,
        surfaces: types.Tuple[types.IntegerOrJump],
        cells: types.Tuple[types.IntegerOrJump],
        options: types.Tuple[ssw.SswOption_] = None,
    ):
        """
        Initializes ``Ssw``.

        Parameters:
            surfaces: Problem surfaces.
            cells: Problem cells.
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if surfaces is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, surfaces)
        if cells is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, cells)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                surfaces,
                cells,
                options,
            ]
        )

        self.surfaces: typing.Final[types.Tuple[types.IntegerOrJump]] = surfaces
        self.cells: typing.Final[types.Tuple[types.IntegerOrJump]] = cells
        self.options: typing.Final[types.Tuple[ssw.SswOption_]] = options
