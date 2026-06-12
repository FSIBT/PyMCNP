import typing
import decimal
import collections
import dataclasses

from ... import _show
from ... import abc
from ..Card import Card
from .. import literal
from .. import option


class Cell(Card):
    """
    Represents cell cards.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    def __invert__(self) -> literal.Geometry:
        """
        Complements cell cards.

        Returns:
            Geometry of cell cards.
        """

        assert hasattr(self, 'j')

        return literal.Geometry.from_mcnp(f'#{self.j}')[0]


class Cell_0(Cell):
    """
    Represents cell cards, form #0.

    Attributes:
        j: cell card `j` parameter.
        m: cell card `m` parameter.
        d: cell card `d` parameter.
        geom: cell card `geom` parameter.
        options: cell card `options` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    j: literal.Integer | int | str
    m: literal.Integer | int | str
    d: literal.Real | int | float | decimal.Decimal | str
    geom: literal.Geometry | str
    options: typing.Annotated[abc.Array, option.Cell, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[option.Cell | str] | str = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates cell cards, form #0.

        Raises:
            Error: Invalid value.
        """

        assert isinstance(self.j, literal.Integer)
        assert isinstance(self.m, literal.Integer)

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
        """

        assert isinstance(self.geom, literal.Geometry)

        return self.geom.to_show(surfaces, cells)


class Cell_1(Cell):
    """
    Represents cell cards, form #1.

    Attributes:
        j: cell card `j` parameter.
        m: cell card `m` parameter.
        geom: cell card `geom` parameter.
        options: cell card `options` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    j: literal.Integer | int | str
    m: literal.Integer | int | str
    geom: literal.Geometry | str
    options: typing.Annotated[abc.Array, option.Cell, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[option.Cell | str] | str = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates cell cards, form #0.

        Raises:
            Error: Invalid value.
        """

        assert isinstance(self.j, literal.Integer)
        assert isinstance(self.m, literal.Integer)
        assert isinstance(self.options, (abc.Array, abc.Terminal[r'']))

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
        """

        assert isinstance(self.geom, literal.Geometry)

        return self.geom.to_show(surfaces, cells)


class Cell_2(Cell):
    """
    Represents cell cards, form #2.

    Attributes:
        j: cell card `j` parameter.
        like: cell card `LIKE` symbol.
        n: cell card `n` parameter.
        but: cell card `BUT` symbol.
        options: cell card `options` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    j: literal.Integer | int | str
    like: typing.Annotated[abc.Terminal, r'LIKE'] | str = abc.Terminal[r'LIKE']('LIKE')
    n: literal.Integer | int | str
    but: typing.Annotated[abc.Terminal, r'BUT'] | str = abc.Terminal[r'BUT']('BUT')
    options: typing.Annotated[abc.Array, option.Cell, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[option.Cell | str] | str = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates cell cards, form #1.

        Raises:
            Error: Invalid value.
        """

        assert isinstance(self.j, literal.Integer)
        assert isinstance(self.n, literal.Integer)

        if not (1 <= self.j <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.j=}')

        if not (1 <= self.n <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.n=}')

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
