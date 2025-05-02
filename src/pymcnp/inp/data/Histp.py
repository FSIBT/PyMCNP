import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types


class Histp(DataOption):
    """
    Represents INP histp elements.

    Attributes:
        lhist: Number of words written to a HISTP file.
        cells: Cell numbers.
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
            InpError: SEMANTICS_OPTION.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                lhist,
                cells,
            ]
        )

        self.lhist: typing.Final[types.IntegerOrJump] = lhist
        self.cells: typing.Final[types.Tuple[types.IntegerOrJump]] = cells


@dataclasses.dataclass
class HistpBuilder:
    """
    Builds ``Histp``.

    Attributes:
        lhist: Number of words written to a HISTP file.
        cells: Cell numbers.
    """

    lhist: str | int | types.IntegerOrJump = None
    cells: list[str] | list[int] | list[types.IntegerOrJump] = None

    def build(self):
        """
        Builds ``HistpBuilder`` into ``Histp``.

        Returns:
            ``Histp`` for ``HistpBuilder``.
        """

        lhist = None
        if isinstance(self.lhist, types.Integer):
            lhist = self.lhist
        elif isinstance(self.lhist, int):
            lhist = types.IntegerOrJump(self.lhist)
        elif isinstance(self.lhist, str):
            lhist = types.IntegerOrJump.from_mcnp(self.lhist)

        cells = []
        for item in self.cells:
            if isinstance(item, types.IntegerOrJump):
                cells.append(item)
            elif isinstance(item, int):
                cells.append(types.IntegerOrJump(item))
            elif isinstance(item, str):
                cells.append(types.IntegerOrJump.from_mcnp(item))
        cells = types.Tuple(cells)

        return Histp(
            lhist=lhist,
            cells=cells,
        )
