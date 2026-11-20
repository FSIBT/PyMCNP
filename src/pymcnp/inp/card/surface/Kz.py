import typing

import numpy

from .... import abc
from .... import _show
from ... import literal
from ..Surface import Surface


class Kz(Surface):
    """
    Represents kz surface cards.

    Attributes:
        prefix: kz surface card ``prefix`` parameter.
        j: kz surface card ``j`` parameter.
        n: kz surface card ``n`` parameter.
        keyword: kz surface card ``r'KZ'`` symbol.
        z: kz surface card ``z`` parameter.
        t_squared: kz surface card ``t_squared`` parameter.
        plus_minus_1: kz surface card ``plus_minus_1`` parameter.
    """

    prefix: typing.Annotated[abc.Terminal, r'[+*]'] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    j: literal.Integer
    n: literal.Integer | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    keyword: typing.Annotated[abc.Terminal, r'KZ'] = abc.Terminal[r'KZ']('KZ')
    z: literal.Real
    t_squared: literal.Real
    plus_minus_1: literal.Real

    def __post_init__(self) -> None:
        """
        Validates kz surface cards.

        Raises:
            Error: Invalid value.
        """

        if not (1 <= self.j <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.j=}')

        if isinstance(self.n, literal.Integer) and not (1 <= self.n <= 999):
            raise abc.Error('Invalid value.', f'{self.n=}')

    def to_show(self, shapes: abc.Endpoint = _show.pyvista) -> abc.Visualization:
        """
        Visualizes kz surface cards.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            Visualizations of kz surface cards.
        """

        vis = shapes.ConeUnbounded(float(self.t_squared) ** (1 / 2), int(self.plus_minus_1))
        vis = vis.translate(numpy.array((0, 0, float(self.z))))

        return vis
