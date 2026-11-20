import typing

import numpy

from .... import abc
from .... import _show
from ... import literal
from ..Surface import Surface


class Cx(Surface):
    """
    Represents cx surface cards.

    Attributes:
        prefix: cx surface card ``prefix`` parameter.
        j: cx surface card ``j`` parameter.
        n: cx surface card ``n`` parameter.
        keyword: cx surface card ``r'CX'`` symbol.
        r: cx surface card ``R`` parameter.
    """

    prefix: typing.Annotated[abc.Terminal, r'[+*]'] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    j: literal.Integer
    n: literal.Integer | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    keyword: typing.Annotated[abc.Terminal, r'CX'] = abc.Terminal[r'CX']('CX')
    r: literal.Real

    def __post_init__(self) -> None:
        """
        Validates cx surface cards.

        Raises:
            Error: Invalid value.
        """

        if not (1 <= self.j <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.j=}')

        if isinstance(self.n, literal.Integer) and not (1 <= self.n <= 999):
            raise abc.Error('Invalid value.', f'{self.n=}')

    def to_show(self, shapes: abc.Endpoint = _show.pyvista) -> abc.Visualization:
        """
        Visualizes cx surface cards.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            Visualizations of cx surface cards.
        """

        vis = shapes.CylinderUnbounded(float(self.r))
        vis = vis.rotate(numpy.array((0, 1, 0)), 90, numpy.zeros(3))

        return vis
