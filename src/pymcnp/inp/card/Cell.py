from __future__ import annotations

import abc as abc_
import typing

from ... import _show
from ... import abc
from ..Card import Card
from .. import literal
from .. import option
from ..literal.Geometry import Missing


class Cell(Card):
    """
    Represents cell cards.
    """

    if typing.TYPE_CHECKING:
        j: literal.Integer
        options: typing.Annotated[abc.Array, option.Cell, None] | typing.Annotated[abc.Terminal, r'']

    def __invert__(self) -> literal.Geometry:
        """
        Complements cell cards.

        Returns:
            Geometry of cell cards.
        """

        return literal.Geometry.from_mcnp(f'#{self.j}')[0]

    @abc_.abstractmethod
    def material(self, cells: tuple[Cell, ...]) -> literal.Integer:
        """
        Gets material number of cell cards.

        Parameters:
            cells: Sibling cells in cell block.

        Returns:
            Resolved cell card material number.
        """

        raise NotImplementedError

    @abc_.abstractmethod
    def density(self, cells: tuple[Cell, ...]) -> literal.Real | None:
        """
        Gets density number of cell cards.

        Parameters:
            cells: Sibling cells in cell block.

        Returns:
            Resolved cell card density number.
        """

        raise NotImplementedError


class Cell_0(Cell):
    """
    Represents cell cards, form #0: a cell with material ``m`` (not 0) and density ``d``, ``j m d geom params``.

    Attributes:
        j: cell card ``j`` parameter.
        m: cell card ``m`` parameter.
        d: cell card ``d`` parameter.
        geom: cell card ``geom`` parameter.
        options: cell card ``options`` parameter.
    """

    j: literal.Integer
    m: literal.Integer
    d: literal.Real
    geom: literal.Geometry
    options: typing.Annotated[abc.Array, option.Cell, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates cell cards, form #0.

        Raises:
            Error: Invalid value.
        """

        if not (1 <= self.j <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.j=}')

        if not (1 <= self.m <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.m=}')

        if isinstance(self.options, abc.Array) and any(isinstance(keyvalue, (option.cell.Rho, option.cell.Mat)) for keyvalue in self.options):
            raise abc.Error('Invalid value.', f'{self.options=}')

    def to_show(self, surfaces: dict[str, abc.Visualization], cells: dict[str, abc.Visualization], shapes: abc.Endpoint = _show.pyvista) -> abc.Visualization:
        """
        Visualizes cell cards.

        Parameters:
            surfaces: Visualizations of surface cards.
            cells: Visualizations of cell cards.
            shapes: Collection of shapes.

        Returns:
            Visualization of cell cards.

        Raises:
            Error: The cell refers to a cell or surface that is not in the file.
        """

        try:
            return self.geom.to_show(surfaces, cells)
        except Missing as err:
            raise abc.Error(f'Cell {self.j} refers to {err.kind} {err.number}, which is not in the file.', self.to_mcnp()) from None

    def material(self, cells: tuple[Cell, ...]) -> literal.Integer:
        """
        Gets material number of cell cards.

        Parameters:
            cells: Sibling cells in cell block.

        Returns:
            Resolved cell card material number.
        """

        return self.m

    def density(self, cells: tuple[Cell, ...]) -> literal.Real | None:
        """
        Gets density number of cell cards.

        Parameters:
            cells: Sibling cells in cell block.

        Returns:
            Resolved cell card density number.
        """

        return self.d


class Cell_1(Cell):
    """
    Represents cell cards, form #1: a void cell, ``j 0 geom params``.

    Attributes:
        j: cell card ``j`` parameter.
        m: cell card ``m`` parameter.
        geom: cell card ``geom`` parameter.
        options: cell card ``options`` parameter.
    """

    j: literal.Integer
    m: literal.Integer
    geom: literal.Geometry
    options: typing.Annotated[abc.Array, option.Cell, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates cell cards, form #0.

        Raises:
            Error: Invalid value.
        """

        if not (1 <= self.j <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.j=}')

        if not self.m == 0:
            raise abc.Error('Invalid value.', f'{self.m=}')

        if isinstance(self.options, abc.Array) and any(isinstance(keyvalue, (option.cell.Rho, option.cell.Mat)) for keyvalue in self.options):
            raise abc.Error('Invalid value.', f'{self.options=}')

    def to_show(self, surfaces: dict[str, abc.Visualization], cells: dict[str, abc.Visualization], shapes: abc.Endpoint = _show.pyvista) -> abc.Visualization:
        """
        Visualizes cell cards.

        Parameters:
            surfaces: Visualizations of surface cards.
            cells: Visualizations of cell cards.
            shapes: Collection of shapes.

        Returns:
            Visualization of cell cards.

        Raises:
            Error: The cell refers to a cell or surface that is not in the file.
        """

        try:
            return self.geom.to_show(surfaces, cells)
        except Missing as err:
            raise abc.Error(f'Cell {self.j} refers to {err.kind} {err.number}, which is not in the file.', self.to_mcnp()) from None

    def material(self, cells: tuple[Cell, ...]) -> literal.Integer:
        """
        Gets material number of cell cards.

        Parameters:
            cells: Sibling cells in cell block.

        Returns:
            Resolved cell card material number.
        """

        return self.m

    def density(self, cells: tuple[Cell, ...]) -> literal.Real | None:
        """
        Gets density number of cell cards.

        Parameters:
            cells: Sibling cells in cell block.

        Returns:
            Resolved cell card density number.
        """

        return None


class Cell_2(Cell):
    """
    Represents cell cards, form #2: a cell like another, ``j LIKE n BUT params``.

    Attributes:
        j: cell card ``j`` parameter.
        like: cell card ``r'LIKE'`` symbol.
        n: cell card ``n`` parameter.
        but: cell card ``r'BUT'`` symbol.
        options: cell card ``options`` parameter.
    """

    j: literal.Integer
    like: typing.Annotated[abc.Terminal, r'LIKE'] = abc.Terminal[r'LIKE']('LIKE')
    n: literal.Integer
    but: typing.Annotated[abc.Terminal, r'BUT'] = abc.Terminal[r'BUT']('BUT')
    options: typing.Annotated[abc.Array, option.Cell, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates cell cards, form #1.

        Raises:
            Error: Invalid value.
        """

        if not (1 <= self.j <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.j=}')

        if not (1 <= self.n <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.n=}')

        if not (self.j != self.n):
            raise abc.Error('Invalid value.', f'({self.n=}) == ({self.j=})')

    def to_show(self, surfaces: dict[str, abc.Visualization], cells: dict[str, abc.Visualization], shapes: abc.Endpoint = _show.pyvista) -> abc.Visualization:
        """
        Visualizes cell cards.

        Parameters:
            surfaces: Visualizations of surface cards.
            cells: Visualizations of cell cards.
            shapes: Collection of shapes.

        Returns:
            Visualization of cell cards.
        """

        return cells[str(self.n)]

    def material(self, cells: tuple[Cell, ...]) -> literal.Integer:
        """
        Gets material number of cell cards.

        Parameters:
            cells: Sibling cells in cell block.

        Returns:
            Resolved cell card material number.

        Raises:
            Error: Invalid value.
        """

        if isinstance(self.options, abc.Array):
            mat = self.options.filter(option.cell.Mat)
            if len(mat) > 0:
                return mat[0].m

        for cell in reversed(cells):
            if cell.j == self.n:
                return cell.material(cells)

        raise abc.Error('Invalid value.', f'{self=}')

    def density(self, cells: tuple[Cell, ...]) -> literal.Real | None:
        """
        Gets density number of cell cards.

        Parameters:
            cells: Sibling cells in cell block.

        Returns:
            Resolved cell card density number.
        """

        if isinstance(self.options, abc.Array):
            rho = self.options.filter(option.cell.Rho)
            if len(rho) > 0:
                return rho[0].d

        for cell in reversed(cells):
            if cell.j == self.n:
                return cell.density(cells)

        return None
