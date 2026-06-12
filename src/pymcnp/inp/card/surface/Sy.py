import typing
import decimal
import dataclasses

import numpy

from .... import abc
from .... import _show
from ... import literal
from ..Surface import Surface


class Sy(Surface):
    """
    Represents sy surface cards.

    Attributes:
        prefix: sy surface card `prefix` parameter.
        j: sy surface card `j` parameter.
        n: sy surface card `n` parameter.
        keyword: sy surface card `SY` symbol.
        y: sy surface card `y` parameter.
        r: sy surface card `R` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    prefix: typing.Annotated[abc.Terminal, r'[+*]'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    j: literal.Integer | int | str
    n: literal.Integer | typing.Annotated[abc.Terminal, r''] | int | str = abc.Terminal[r'']('')
    keyword: typing.Annotated[abc.Terminal, r'SY'] | str = abc.Terminal[r'SY']('SY')
    y: literal.Real | int | float | decimal.Decimal | str
    r: literal.Real | int | float | decimal.Decimal | str

    def __post_init__(self) -> None:
        """
        Validates sy surface cards.

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
        Visualizes sy surface cards.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            Visualizations of sy surface cards.
        """

        vis = shapes.Sphere(float(self.r))
        vis = vis.rotate(numpy.array((1, 0, 0)), 90, numpy.zeros(3))
        vis = vis.translate(numpy.array((0, float(self.y), 0)))

        return vis
