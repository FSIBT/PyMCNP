import typing
import decimal
import dataclasses

import numpy

from .... import abc
from .... import _show
from ... import literal
from ..Surface import Surface


class C_x(Surface):
    """
    Represents c/x surface cards.

    Attributes:
        prefix: c/x surface card `prefix` parameter.
        j: c/x surface card `j` parameter.
        n: c/x surface card `n` parameter.
        keyword: c/x surface card `C/X` symbol.
        y: c/x surface card `y` parameter.
        z: c/x surface card `z` parameter.
        r: c/x surface card `R` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    prefix: typing.Annotated[abc.Terminal, r'[+*]'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    j: literal.Integer | int | str
    n: literal.Integer | typing.Annotated[abc.Terminal, r''] | int | str = abc.Terminal[r'']('')
    keyword: typing.Annotated[abc.Terminal, r'C/X'] | str = abc.Terminal[r'C/X']('C/X')
    y: literal.Real | int | float | decimal.Decimal | str
    z: literal.Real | int | float | decimal.Decimal | str
    r: literal.Real | int | float | decimal.Decimal | str

    def __post_init__(self) -> None:
        """
        Validates c/x surface cards.

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
        Visualizes c/x surface cards.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            Visualizations of c/x surface cards.
        """

        vis = shapes.CylinderUnbounded(float(self.r))
        vis = vis.rotate(numpy.array((0, 1, 0)), 90, numpy.zeros(3))
        vis = vis.translate(numpy.array((0, float(self.y), float(self.z))))

        return vis
