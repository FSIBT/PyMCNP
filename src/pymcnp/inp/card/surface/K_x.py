import typing
import decimal
import dataclasses

import numpy

from .... import abc
from .... import _show
from ... import literal
from ..Surface import Surface


class K_x(Surface):
    """
    Represents k/x surface cards.

    Attributes:
        prefix: k/x surface card `prefix` parameter.
        j: k/x surface card `j` parameter.
        n: k/x surface card `n` parameter.
        keyword: k/x surface card `K/X` symbol.
        x: k/x surface card `x` parameter.
        y: k/x surface card `y` parameter.
        z: k/x surface card `z` parameter.
        t_squared: k/x surface card `t_squared` parameter.
        plus_minus_1: k/x surface card `plus_minus_1` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    prefix: typing.Annotated[abc.Terminal, r'[+*]'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    j: literal.Integer | int | str
    n: literal.Integer | typing.Annotated[abc.Terminal, r''] | int | str = abc.Terminal[r'']('')
    keyword: typing.Annotated[abc.Terminal, r'K/X'] | str = abc.Terminal[r'K/X']('K/X')
    x: literal.Real | int | float | decimal.Decimal | str
    y: literal.Real | int | float | decimal.Decimal | str
    z: literal.Real | int | float | decimal.Decimal | str
    t_squared: literal.Real | int | float | decimal.Decimal | str
    plus_minus_1: literal.Real | int | float | decimal.Decimal | str

    def __post_init__(self) -> None:
        """
        Validates k/x surface cards.

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
        Visualizes k/x surface cards.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            Visualizations of k/x surface cards.
        """

        vis = shapes.ConeUnbounded(float(self.t_squared) ** (1 / 2), int(self.plus_minus_1))
        vis = vis.rotate(numpy.array((0, 1, 0)), 90, numpy.zeros(3))
        vis = vis.translate(numpy.array((float(self.x), float(self.y), float(self.z))))

        return vis
