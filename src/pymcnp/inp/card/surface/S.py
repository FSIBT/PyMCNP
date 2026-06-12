import typing
import decimal
import dataclasses

import numpy

from .... import abc
from .... import _show
from ... import literal
from ..Surface import Surface


class S(Surface):
    """
    Represents s surface cards.

    Attributes:
        prefix: s surface card `prefix` parameter.
        j: s surface card `j` parameter.
        n: s surface card `n` parameter.
        keyword: s surface card `S` symbol.
        x: s surface card `x` parameter.
        y: s surface card `y` parameter.
        z: s surface card `z` parameter.
        r: s surface card `R` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    prefix: typing.Annotated[abc.Terminal, r'[+*]'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    j: literal.Integer | int | str
    n: literal.Integer | typing.Annotated[abc.Terminal, r''] | int | str = abc.Terminal[r'']('')
    keyword: typing.Annotated[abc.Terminal, r'S'] | str = abc.Terminal[r'S']('S')
    x: literal.Real | int | float | decimal.Decimal | str
    y: literal.Real | int | float | decimal.Decimal | str
    z: literal.Real | int | float | decimal.Decimal | str
    r: literal.Real | int | float | decimal.Decimal | str

    def __post_init__(self) -> None:
        """
        Validates s surface cards.

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
        Visualizes s surface cards.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            Visualizations of s surface cards.
        """

        vis = shapes.Sphere(float(self.r))
        vis = vis.translate(numpy.array((float(self.x), float(self.y), float(self.z))))

        return vis
