import re

from . import _card
from .. import types


class Histp(_card.Card):
    """
    Represents INP `histp` cards.
    """

    _KEYWORD = 'histp'

    _ATTRS = {
        'lhist': types.Integer,
        'cells': types.Tuple(types.Integer),
    }

    _REGEX = re.compile(rf'\Ahistp( {types.Integer._REGEX.pattern[2:-2]})?((?: {types.Integer._REGEX.pattern[2:-2]})+?)?\Z', re.IGNORECASE)

    def __init__(self, lhist: str | int | types.Integer = None, cells: list[str] | list[int] | list[types.Integer] = None):
        """
        Initializes `Histp`.

        Parameters:
            lhist: Number of words written to a HISTP file.
            cells: Cell numbers.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.lhist: types.Integer = lhist
        self.cells: types.Tuple(types.Integer) = cells

    @property
    def lhist(self) -> types.Integer:
        """
        Number of words written to a HISTP file

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._lhist

    @lhist.setter
    def lhist(self, lhist: str | int | types.Integer) -> None:
        """
        Sets `lhist`.

        Parameters:
            lhist: Number of words written to a HISTP file.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if lhist is not None:
            if isinstance(lhist, types.Integer):
                lhist = lhist
            elif isinstance(lhist, int):
                lhist = types.Integer(lhist)
            elif isinstance(lhist, str):
                lhist = types.Integer.from_mcnp(lhist)

        self._lhist: types.Integer = lhist

    @property
    def cells(self) -> types.Tuple(types.Integer):
        """
        Cell numbers

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._cells

    @cells.setter
    def cells(self, cells: list[str] | list[int] | list[types.Integer]) -> None:
        """
        Sets `cells`.

        Parameters:
            cells: Cell numbers.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if cells is not None:
            array = []
            for item in cells:
                if isinstance(item, types.Integer):
                    array.append(item)
                elif isinstance(item, int):
                    array.append(types.Integer(item))
                elif isinstance(item, str):
                    array.append(types.Integer.from_mcnp(item))
            cells = types.Tuple(types.Integer)(array)

        self._cells: types.Tuple(types.Integer) = cells
