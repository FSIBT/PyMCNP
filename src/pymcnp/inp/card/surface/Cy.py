import typing

import numpy

from .... import abc
from .... import _show
from ... import literal
from ..Surface import Surface


class Cy(Surface):
    """
    Represents cy surface cards.

    Attributes:
        prefix: cy surface card ``prefix`` parameter.
        j: cy surface card ``j`` parameter.
        n: cy surface card ``n`` parameter.
        keyword: cy surface card ``r'CY'`` symbol.
        r: cy surface card ``R`` parameter.
    """

    prefix: typing.Annotated[abc.Terminal, r'[+*]'] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    j: literal.Integer
    n: literal.Integer | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    keyword: typing.Annotated[abc.Terminal, r'CY'] = abc.Terminal[r'CY']('CY')
    r: literal.Real

    def __post_init__(self) -> None:
        """
        Validates cy surface cards.

        Raises:
            Error: Invalid value.
        """

        if not (1 <= self.j <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.j=}')

        if isinstance(self.n, literal.Integer) and not (1 <= self.n <= 999):
            raise abc.Error('Invalid value.', f'{self.n=}')

    def to_show(self, shapes: abc.Endpoint = _show.pyvista) -> abc.Visualization:
        """
        Visualizes cy surface cards.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            Visualizations of cy surface cards.
        """

        vis = shapes.CylinderUnbounded(float(self.r))
        vis = vis.rotate(numpy.array((1, 0, 0)), 90, numpy.zeros(3))

        return vis
