import typing
import decimal
import dataclasses

import numpy

from .... import abc
from .... import _show
from ... import literal
from ..Surface import Surface


class C_z(Surface):
    """
    Represents c/z surface cards.

    Attributes:
        prefix: c/z surface card `prefix` parameter.
        j: c/z surface card `j` parameter.
        n: c/z surface card `n` parameter.
        keyword: c/z surface card `C/Z` symbol.
        x: c/z surface card `x` parameter.
        y: c/z surface card `y` parameter.
        R: c/z surface card `R` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    prefix: typing.Annotated[abc.Terminal, r'[+*]'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    j: literal.Integer | int | str
    n: literal.Integer | typing.Annotated[abc.Terminal, r''] | int | str = abc.Terminal[r'']('')
    keyword: typing.Annotated[abc.Terminal, r'C/Z'] | str = abc.Terminal[r'C/Z']('C/Z')
    x: literal.Real | int | float | decimal.Decimal | str
    y: literal.Real | int | float | decimal.Decimal | str
    r: literal.Real | int | float | decimal.Decimal | str

    def __post_init__(self) -> None:
        """
        Validates c/z surface cards.

        Raises:
            Error: Invalid value.
        """

        assert isinstance(self.j, literal.Integer)
        assert isinstance(self.n, (literal.Integer, abc.Terminal[r'']))

        if not (1 <= self.j <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.j=}')

        if isinstance(self.n, literal.Integer) and not (1 <= self.n <= 999):
            raise abc.Error('Invalid value.', f'{self.n=}')

    def to_show(self, shapes: abc.Endpoint = _show.pyvista) -> abc.Visualization:
        """
        Visualizes c/z surface cards.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            Visualizations of c/z surface cards.
        """

        vis = shapes.CylinderUnbounded(float(self.r))
        vis = vis.rotate(numpy.array((0, 1, 0)), 90, numpy.zeros(3))
        vis = vis.translate(numpy.array((float(self.x), float(self.y), 0)))

        return vis
