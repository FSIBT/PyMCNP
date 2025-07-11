import re

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

    def __init__(self, lhist: str | int | types.Integer = None, cells: list[str] | list[int] | list[types.Integer] = None):
        """
        Initializes ``Histp``.

        Parameters:
            lhist: Number of words written to a HISTP file.
            cells: Cell numbers.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.lhist: types.Integer = lhist
        self.cells: types.Tuple[types.Integer] = cells

    @property
    def lhist(self) -> types.Integer:
        """
        Gets ``lhist``.

        Returns:
            ``lhist``.
        """

        return self._lhist

    @lhist.setter
    def lhist(self, lhist: str | int | types.Integer) -> None:
        """
        Sets ``lhist``.

        Parameters:
            lhist: Number of words written to a HISTP file.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if lhist is not None:
            if isinstance(lhist, types.Integer):
                lhist = lhist
            elif isinstance(lhist, int):
                lhist = types.Integer(lhist)
            elif isinstance(lhist, str):
                lhist = types.Integer.from_mcnp(lhist)
            else:
                raise TypeError

        self._lhist: types.Integer = lhist

    @property
    def cells(self) -> types.Tuple[types.Integer]:
        """
        Gets ``cells``.

        Returns:
            ``cells``.
        """

        return self._cells

    @cells.setter
    def cells(self, cells: list[str] | list[int] | list[types.Integer]) -> None:
        """
        Sets ``cells``.

        Parameters:
            cells: Cell numbers.

        Raises:
            InpError: SEMANTICS_OPTION.
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
                else:
                    raise TypeError
            cells = types.Tuple(array)

        self._cells: types.Tuple[types.Integer] = cells
