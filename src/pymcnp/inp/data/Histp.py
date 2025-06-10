import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types


class Histp(_option.DataOption):
    """
    Represents INP histp elements.

    Attributes:
        lhist: Number of words written to a HISTP file.
        cells: Cell numbers.
    """

    _KEYWORD = 'histp'

    _ATTRS = {
        'lhist': types.Integer,
        'cells': types.Tuple[types.Integer],
    }

    _REGEX = re.compile(rf'\Ahistp( {types.Integer._REGEX.pattern[2:-2]})?((?: {types.Integer._REGEX.pattern[2:-2]})+?)?\Z')

    def __init__(self, lhist: types.Integer = None, cells: types.Tuple[types.Integer] = None):
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

        self.lhist: typing.Final[types.Integer] = lhist
        self.cells: typing.Final[types.Tuple[types.Integer]] = cells


@dataclasses.dataclass
class HistpBuilder(_option.DataOptionBuilder):
    """
    Builds ``Histp``.

    Attributes:
        lhist: Number of words written to a HISTP file.
        cells: Cell numbers.
    """

    lhist: str | int | types.Integer = None
    cells: list[str] | list[int] | list[types.Integer] = None

    def build(self):
        """
        Builds ``HistpBuilder`` into ``Histp``.

        Returns:
            ``Histp`` for ``HistpBuilder``.
        """

        lhist = self.lhist
        if isinstance(self.lhist, types.Integer):
            lhist = self.lhist
        elif isinstance(self.lhist, int):
            lhist = types.Integer(self.lhist)
        elif isinstance(self.lhist, str):
            lhist = types.Integer.from_mcnp(self.lhist)

        if self.cells:
            cells = []
            for item in self.cells:
                if isinstance(item, types.Integer):
                    cells.append(item)
                elif isinstance(item, int):
                    cells.append(types.Integer(item))
                elif isinstance(item, str):
                    cells.append(types.Integer.from_mcnp(item))
            cells = types.Tuple(cells)
        else:
            cells = None

        return Histp(
            lhist=lhist,
            cells=cells,
        )

    @staticmethod
    def unbuild(ast: Histp):
        """
        Unbuilds ``Histp`` into ``HistpBuilder``

        Returns:
            ``HistpBuilder`` for ``Histp``.
        """

        return HistpBuilder(
            lhist=copy.deepcopy(ast.lhist),
            cells=copy.deepcopy(ast.cells),
        )
