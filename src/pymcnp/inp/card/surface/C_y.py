import typing

import numpy

from .... import abc
from .... import _show
from ... import literal
from ..Surface import Surface


class C_y(Surface):
    """
    Represents c/y surface cards.

    Attributes:
        prefix: c/y surface card ``prefix`` parameter.
        j: c/y surface card ``j`` parameter.
        n: c/y surface card ``n`` parameter.
        keyword: c/y surface card ``r'C/Y'`` symbol.
        x: c/y surface card ``x`` parameter.
        z: c/y surface card ``z`` parameter.
        r: c/y surface card ``R`` parameter.
    """

    prefix: typing.Annotated[abc.Terminal, r'[+*]'] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    j: literal.Integer
    n: literal.Integer | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    keyword: typing.Annotated[abc.Terminal, r'C/Y'] = abc.Terminal[r'C/Y']('C/Y')
    x: literal.Real
    z: literal.Real
    r: literal.Real

    def __post_init__(self) -> None:
        """
        Validates c/y surface cards.

        Raises:
            Error: Invalid value.
        """

        if not (1 <= self.j <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.j=}')

        if isinstance(self.n, literal.Integer) and not (1 <= self.n <= 999):
            raise abc.Error('Invalid value.', f'{self.n=}')

    def to_show(self, shapes: abc.Endpoint = _show.pyvista) -> abc.Visualization:
        """
        Visualizes c/y surface cards.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            Visualizations of c/y surface cards.
        """

        vis = shapes.CylinderUnbounded(float(self.r))
        vis = vis.rotate(numpy.array((1, 0, 0)), 90, numpy.zeros(3))
        vis = vis.translate(numpy.array((float(self.x), 0, float(self.z))))

        return vis
