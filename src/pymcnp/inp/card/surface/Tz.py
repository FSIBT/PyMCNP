import typing
import decimal
import dataclasses

import numpy

from .... import abc
from .... import _show
from ... import literal
from ..Surface import Surface


class Tz(Surface):
    """
    Represents tz surface cards.

    Attributes:
        prefix: tz surface card `prefix` parameter.
        j: tz surface card `j` parameter.
        n: tz surface card `n` parameter.
        keyword: tz surface card `TZ` symbol.
        x: tz surface card `x` parameter.
        y: tz surface card `y` parameter.
        z: tz surface card `z` parameter.
        a: tz surface card `A` parameter.
        b: tz surface card `B` parameter.
        c: tz surface card `C` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    prefix: typing.Annotated[abc.Terminal, r'[+*]'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    j: literal.Integer | int | str
    n: literal.Integer | typing.Annotated[abc.Terminal, r''] | int | str = abc.Terminal[r'']('')
    keyword: typing.Annotated[abc.Terminal, r'TZ'] | str = abc.Terminal[r'TZ']('TZ')
    x: literal.Real | int | float | decimal.Decimal | str
    y: literal.Real | int | float | decimal.Decimal | str
    z: literal.Real | int | float | decimal.Decimal | str
    a: literal.Real | int | float | decimal.Decimal | str
    b: literal.Real | int | float | decimal.Decimal | str
    c: literal.Real | int | float | decimal.Decimal | str

    def __post_init__(self) -> None:
        """
        Validates tz surface cards.

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
        Visualizes tz surface cards.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            Visualizations of tz surface cards.
        """

        vis = shapes.Torus(float(self.b), float(self.c), float(self.a))
        vis = vis.translate(numpy.array((float(self.x), float(self.y), float(self.z))))

        return vis
